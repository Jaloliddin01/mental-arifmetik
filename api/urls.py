from django.urls import path

from .views import Questions

urlpatterns = [
    path('questions/', Questions.as_view()),
]