from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    datePosted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} Post"