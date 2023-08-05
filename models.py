# quora_app/models.py

from django.contrib.auth.models import User
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_answers')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional user profile fields here if needed
