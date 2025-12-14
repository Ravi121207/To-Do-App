# from django.db import models

# # Create your models here.

# class Task(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     completed = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.title

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False) 
    def __str__(self):
        return self.title
