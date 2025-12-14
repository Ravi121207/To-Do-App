# from django.contrib import admin
# from .models import Task
# # Register your models here.

# @admin.register(Task)
# class TaskAdmin(admin.ModelAdmin):
#     list_display=('title ','complete','create_at')
#     list_filter=('complete','create_at')
#     search_fields=('title','description')
#     ordering=('-create_at')

from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'complete', 'created_at')
    list_filter = ('complete', 'created_at')
    ordering = ('created_at',)
