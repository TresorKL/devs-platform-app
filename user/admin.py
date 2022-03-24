from django.contrib import admin

from .models import User,Project,Tool,Field

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Tool)
admin.site.register(Field)

