from django.contrib import admin

# Register your models here.

from .models import Category, Question

admin.site.register(Category)
admin.site.register(Question)
