from django.urls import path
from . import views

app_name = 'stackbase'

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('questions/',views.QuestionListView.as_view(),name="question_list"),
    path('questions/new',views.QuestionCreateView.as_view(),name="question_create"),
    path('questions/<int:pk>',views.QuestionDetailView.as_view(),name="question_detail"),
    path('questions/<int:pk>/update',views.QuestionUpdateView.as_view(),name="question_update"),
]