from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from numpy import delete

# Create your models here.

class Post(models.Model):
    title= models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    dete_posted = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title