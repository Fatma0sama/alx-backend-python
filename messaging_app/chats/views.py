#!/usr/bin/env python3
"""Views for messaging app"""
from rest_framework import viewsets
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    """API endpoint for conversations"""
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer


class MessageViewSet(viewsets.ModelViewSet):
    """API endpoint for messages"""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
