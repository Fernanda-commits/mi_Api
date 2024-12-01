from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    order = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title