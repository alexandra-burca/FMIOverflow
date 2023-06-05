from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Question

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'base.html')

class QuestionListView(ListView):
    model = Question
    context_object_name = 'question'
    ordering = ['-date_created']

class QuestionDetailView(DetailView):
    model = Question
    context_object_name = 'question'

class QuestionCreateView(CreateView):
    model = Question
    fields =['title','content']
    context_object_name = 'question'
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
    
