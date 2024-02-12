from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from myApp.models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import get_user_model
from myApp.tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

# Create your views here.

def singupPage(request):
    if request.method == 'POST':
        form=customUserForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_active=False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            messages.success(request, 'Registration successful. You are now logged in.')
          
            return redirect("singinPage")
    else:
        form=customUserForm()
        return render(request,"singupPage.html",{'form':form})


def singinPage(request):
    if request.method == 'POST':
        form=CustomerAutenticationForm(request,data=request.POST)
        if form.is_valid():
           
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            
            user=authenticate(username =username,password = password)
            login(request,user)
            return redirect("homePage")
    else:
            form=CustomerAutenticationForm()

    return render(request,"singin.html",{'form':form})

def activate(request,uid64,token):
    User=get_user_model()
    try:
        uid= force_str(urlsafe_base64_decode(uid64))
        user=User.objects.get(pk=uid)

    except:
        user =None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active=True
        user.save()
        return redirect('singinPage')

    print("account activation: ", account_activation_token.check_token(user, token))

    return redirect('singinPage')


def activateEmail(request,user,to_mail):
    mail_sub='Active your user Account'
    message=render_to_string("template_activate.html",{
        'user': user.username,
        'domain':get_current_site(request).domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':account_activation_token.make_token(user),
        'protocol':'https' if request.is_secure() else 'http'
    })
    email= EmailMessage(mail_sub, message, to=[to_mail])
    if email.send():
        messages.success(request,f'Dear')
    else:
        message.error(request,f'not')

        
def logoutPage(request):
    logout(request)
    return redirect("singinPage")

def homePage(request):
    return render(request,"homePage.html")

def Task(request):
   
    if request.method == "POST":
        form=taskForm(request.POST)
        if form.is_valid():
            form2=form.save(commit=False)
            form2.user=request.user
            form2.save()
            return redirect("viewTask")
    else:
        form=taskForm()
        
    
    return render(request,"Task.html",{'form':form})
 

def viewTask(request):
    task=TaskModel.objects.all()
    form=CatagoriModel.objects.all()
    return render(request,"viewtask.html",{'task':task,'form':form})
  
def completeTask(request,myid):
    task=TaskModel.objects.get(id,id)
    task.completaion =True
    task.save()
    return redirect("viewTask")

def taskEditPage(request, id):
    obj=TaskModel.objects.get(id=id)
    if request.method == 'POST':
        form = taskForm(request.POST, instance=obj) 
        if form.is_valid():
            form.save()
            return redirect("viewTask")

    else:
        form = taskForm(instance=obj) 

    return render(request, 'Edittask.html', {'form': form})

def taskDeletePage(request, id):
    TaskModel.objects.filter(id=id).delete()
    
    messages.success(request, 'Task Delete Successfully!')

    return redirect('viewTask')




def categoryPage(request):
    if request.method == 'POST':
        form = TaskCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('viewTask')
    else:
        form = TaskCategoryForm()

    return render(request, 'categoryPage.html', {'form': form})



