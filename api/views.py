from django.shortcuts import render
from .models import Category, Question
from django.http import JsonResponse, HttpRequest
from django.views import View
# class based views API for getting all categories and questions

class Questions(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        questions = Question.objects.all()
        data = {
            'questions': list(questions.values())
        }
        return JsonResponse(data)

