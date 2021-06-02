# core/admin.py

# Django modules
from django.contrib import admin

# Django locals
from app.core.models import Movie, Person, Role 

# Register your models here.
admin.site.register(Movie)
admin.site.register(Person)
admin.site.register(Role)