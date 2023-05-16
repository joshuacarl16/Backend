# models.py
from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    categoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.categoryName

class Topic(models.Model):
    topicName = models.CharField(max_length=100)
    content = models.TextField()
    categoryName = models.ForeignKey(Category, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topicName

class Comment(models.Model):
    content = models.TextField()
    topicName = models.ForeignKey(Topic, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
