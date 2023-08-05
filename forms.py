

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Question, Answer

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text']
