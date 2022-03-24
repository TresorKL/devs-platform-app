from dataclasses import field
from .models import User
from django.shortcuts import render




def user(request):
    userset = User.objects.all()
    
    return render(request, "users/userpage.html",{'userset': userset}) 
 

def projects(request,pk):
    userOne = User.objects.get(id=pk)
    projects = userOne.projects.all()
    #tools= projects.tool.all()
    #field = projects.field.all()
    #description = projects.description.all()
    return render(request,"users/projectspage.html",{"projects":projects,"user":userOne})
