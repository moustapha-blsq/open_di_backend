from django.contrib import admin
from django.urls import path
from .views import RegisterView, LoginView, UserView, logoutView, UserList

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', logoutView.as_view()),
    path('users', UserList.as_view())

]