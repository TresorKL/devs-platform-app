from django.urls import path
from user import views


urlpatterns = [
     
     path('', views.user,name="users"),
     path('projectspage.html/<str:pk>', views.projects,name="projects")
]