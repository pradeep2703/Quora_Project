

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, QuestionForm, AnswerForm
from .models import Question, Answer

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    questions = Question.objects.all()
    return render(request, 'home.html', {'questions': questions})

@login_required
def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'post_question.html', {'form': form})

@login_required
def answer_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect('home')
    else:
        form = AnswerForm()
    return render(request, 'answer_question.html', {'form': form, 'question': question})

@login_required
def like_answer(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    answer.likes.add(request.user)
    return redirect('home')
