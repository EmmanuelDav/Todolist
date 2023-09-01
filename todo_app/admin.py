from django.contrib import admin

# Register your models here.
from todo_app.models import ToDoItem, ToDoList

admin.site.register(ToDoList)
admin.site.register(ToDoItem)