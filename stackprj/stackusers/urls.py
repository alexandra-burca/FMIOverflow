from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register",views.registerPage,name="register"),
    path("login",views.loginPage,name="login"),
    path("profile",views.profilePage,name="profile"),
    #path("logout",views.logoutPage,name="logout"),
    path('logout',auth_views.LogoutView.as_view(template_name="stackusers/logout.html"),name="logout"),
]