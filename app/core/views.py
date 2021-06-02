# core/views.py

# Django modules
from django.shortcuts import render
from django.views.generic import ListView

# Django locals
from app.core.models import Movie	

# Create your views here.

class MovieList(ListView):
	model = Movie
