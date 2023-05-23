from django.urls import path
from . import views

app_name = 'stackbase'

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('questions/',views.QuestionListView.as_view(),name="question_list"),
]