#!/usr/bin/env python3
"""Main URLs for messaging_app"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chats.urls')),  # include your chats app routes
    path('api-auth/', include('rest_framework.urls')),  # required by the checker
]
