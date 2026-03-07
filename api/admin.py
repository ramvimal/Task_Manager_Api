from django.contrib import admin
from . models import project , Task , Comment
# Register your models here.


class TaskModel(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')

class ProjectModel(admin.ModelAdmin):
    list_display = ('id', 'name')

class CommentModel(admin.ModelAdmin):
    list_display = ('user','task','text','id')

admin.site.register(Comment,CommentModel)
admin.site.register(Task,TaskModel)
admin.site.register(project,ProjectModel)