from django.db import models

from django.contrib.auth.models import AbstractUser

class Custom_User(AbstractUser):
    USER = [
      
        ('student','Student'),
        ('adminuser','Adminuser')
    ]
    user_type = models.CharField(choices=USER , max_length=100)
    city=models.CharField(max_length=100,null=True)

class CatagoriModel(models.Model):
    Catagoriy=models.CharField(max_length=100,null=True)

    def __str__(self) -> str:
        return self.Catagoriy

class TaskModel(models.Model):
    PRIORITY_Cohice = [
        ('high','High'),
        ('mediam','Medium'),
        ('low','Low')
    ]
    user=models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100,null=True)
    describtion=models.CharField(max_length=100,null=True)
    due_date=models.DateField(null=True)
    completaion=models.BooleanField(default=False,null=True)
    priority=models.CharField(choices=PRIORITY_Cohice,null=True,max_length=120)
    Catagoriy=models.ForeignKey(CatagoriModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


