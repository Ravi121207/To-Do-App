# from django .contrib import path
from django.urls import path
from .import views

app_name='todo'

urlpatterns = [
    path('check',views.task_list,name='task_list'),
    path('add/',views.task_create,name='task_create'),
    path('edit/<int:pk>/',views.task_edit,name='task_edit'),
    path('delete/<int:pk>/',views.task_delete,name='task_delete'),
    path('toggle/<int:pk>/',views.task_toggle,name='task_toggle')
]
