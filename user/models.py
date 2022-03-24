from dataclasses import field
from plistlib import UID
from pydoc import describe
from time import time
from turtle import title
from unicodedata import name
import uuid
from django.db import models

class User(models.Model):
    name = models.CharField(null=False, max_length=200)
    job = models.CharField(null=False, max_length=200)
    id = models.UUIDField(editable=False, primary_key=True,unique=True,default=uuid.uuid4)
    projects = models.ManyToManyField("project")
    
    def __str__(self):
        return self.name
    

class Project(models.Model):
    
    title= models.CharField(null=False, max_length=200)
    tool = models.ManyToManyField("Tool")
    field = models.ForeignKey("Field", on_delete=models.CASCADE)
    id = models.UUIDField(editable=False, primary_key=True,unique=True,default=uuid.uuid4)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title



class Tool(models.Model):
    name =  models.CharField(null=False, max_length=200)
    id = models.UUIDField(editable=False, primary_key=True,unique=True,default=uuid.uuid4)
    
    def __str__(self):
        return self.name
    
class Field(models.Model):
    name =  models.CharField(null=False, max_length=200)
    id = models.UUIDField(editable=False, primary_key=True,unique=True,default=uuid.uuid4)
    
    def __str__(self):
        return self.name
    
