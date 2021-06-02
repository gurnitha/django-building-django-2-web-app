# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include

# Django locals
import app.core.urls 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(
                app.core.urls, namespace='core')),
]
