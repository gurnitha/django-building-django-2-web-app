# core/urls.py

# Django modules
from django.urls import path 

# Django locals
from app.core import views

app_name = 'core'

urlpatterns = [
	path('movie',
				views.MovieList.as_view(),
				name='MovieList'),
]