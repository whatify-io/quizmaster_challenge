"""quizmaster_challenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path("quizzes/", views.quiz_list, name="quiz_list"),
    path("quizzes/<str:quiz_id>/", views.quiz_detail, name="quiz_detail"),
    path("quizzes/", views.create_new_quiz, name="create_new_quiz"),
    path("quizzes/_submit/<str:quiz_id>/", views.submit_quiz, name="submit_quiz"),
]
