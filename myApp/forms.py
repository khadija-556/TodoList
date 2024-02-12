from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class customUserForm(UserCreationForm):
    username=forms.CharField(widget= forms.TextInput(attrs=
        {
            'class':'form-control',
            'placeholder':'Input your name'
        }
    ))
 
    password1=forms.CharField(widget= forms.PasswordInput(attrs=
        {
            'class':'form-control',
            'placeholder':'Input your password'
        }
    ))
    password2=forms.CharField(widget= forms.PasswordInput(attrs=
        {
            'class':'form-control',
            'placeholder':'Input your confirm passsword'
        }
    ))
    email=forms.EmailField(widget= forms.EmailInput(attrs=
        {
            'class':'form-control',
            'placeholder':'Input your email'
        }
    ))

    
  
    class Meta:
        model=Custom_User
        fields=UserCreationForm.Meta.fields + ('user_type','city','email')

class CustomerAutenticationForm(AuthenticationForm):
    username=forms.CharField(widget= forms.TextInput(attrs=
        {
            'class':'form-control',
            'placeholder':'Input your name'
        }
    ))
 
    password=forms.CharField(widget= forms.PasswordInput(attrs=
        {
            'class':'form-control',
            'placeholder':'Input your password'
        }
    ))
    class Meta:
        model=Custom_User
        fields=['username','passwoard']

class taskForm(forms.ModelForm):
    
 

    class Meta:
        model=TaskModel
        fields=['title','describtion','due_date','completaion','priority','Catagoriy']
        exclude=['user']

class TaskCategoryForm(forms.ModelForm):
    class Meta:
        model = CatagoriModel
        fields = ['Catagoriy']