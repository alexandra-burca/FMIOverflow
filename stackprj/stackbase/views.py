from django.shortcuts import render
from django.views.generic import ListView
from .models import Question

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'base.html')

class QuestionListView(ListView):
    model = Question
    context_object_name = 'question'
