
from django.contrib import admin
from django.urls import path
from .views import LoginUser,RegisterUser, Task, user, completed_task

urlpatterns = [
    path('login/', LoginUser.as_view()),
    path('register/', RegisterUser.as_view()),
    path('user/', user),
    path('task/', Task.as_view()),
    path('task/complete/', completed_task)
]
