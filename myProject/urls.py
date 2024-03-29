"""
URL configuration for myProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', singupPage,name="singupPage"),
    path('singinPage/', singinPage,name="singinPage"),
    path('logoutPage/', logoutPage,name="logoutPage"),
    path('homePage/', homePage,name="homePage"),
    path('Task/', Task,name="Task"),
    path('viewTask/', viewTask,name="viewTask"),
    path('taskEditPage/<str:id>', taskEditPage,name="taskEditPage"),
    path('taskDeletePage/<str:id>', taskDeletePage,name="taskDeletePage"),
    path('categoryPage/', categoryPage,name="categoryPage"),
    path('activate/<uid64>/<token>', activate,name='activate'),

]
