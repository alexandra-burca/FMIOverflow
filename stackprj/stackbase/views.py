from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Question, Comment
from .forms import CommentForm
from django.urls import reverse, reverse_lazy

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
    
class QuestionUpdateView(UpdateView):
    model = Question
    fields =['title','content']
    context_object_name = 'question'
    def form_valid(self, form):
         form.instance.user = self.request.user
         return super().form_valid(form)
    def test_func(self):
         questions = self.get_object()
         if self.request.user == questions.user:
            return True
         return False
class QuestionDeleteView(UserPassesTestMixin,DeleteView):
    model = Question
    context_object_name = 'question'
    success_url="/"

    def test_func(self):
        questions= self.get_object()
        if self.request.user == questions.user:
            return True
        return False
class CommentDeatilView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'stackbase/question_detail.html'

    def form_valid(self,meta):
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('stackbase:question_detail')

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'stackbase/question_answer.html'

    def form_valid(self,form):
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('stackbase:question_list')