#!/usr/bin/env python3
"""Models for messaging app"""
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom user model"""
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=150, null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=128, null=False)
    phone_number = models.CharField(max_length=20, null=True)
    role_choices = [
        ('guest', 'Guest'),
        ('host', 'Host'),
        ('admin', 'Admin')
    ]
    role = models.CharField(max_length=10, choices=role_choices, default='guest')


class Conversation(models.Model):
    """Conversation model that tracks which users are involved"""
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    """Message model"""
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    message_body = models.TextField(null=False)
    sent_at = models.DateTimeField(auto_now_add=True)
