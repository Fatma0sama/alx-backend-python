#!/usr/bin/env python3
"""URLs for chats app"""
from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers as nested_routers
from .views import ConversationViewSet, MessageViewSet

# Main router
router = routers.DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')

# Nested router for messages under conversations
conversation_router = nested_routers.NestedDefaultRouter(router, r'conversations', lookup='conversation')
conversation_router.register(r'messages', MessageViewSet, basename='conversation-messages')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(conversation_router.urls)),
]
