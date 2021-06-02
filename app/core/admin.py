# core/admin.py

# Django modules
from django.contrib import admin

# Django locals
from app.core.models import Movie 

# Register your models here.
admin.site.register(Movie)