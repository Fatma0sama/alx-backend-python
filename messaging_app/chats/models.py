#!/usr/bin/env python3
"""Models for messaging app"""
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom user model"""
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=20, null=True)
    role_choices = [
        ('guest', 'Guest'),
        ('host', 'Host'),
        ('admin', 'Admin')
    ]
    role = models.CharField(max_length=10, choices=role_choices, default='guest')


class Conversation(models.Model):
    """Conversation between users"""
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participants = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    """Message sent in a conversation"""
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
