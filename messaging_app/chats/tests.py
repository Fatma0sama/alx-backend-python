#!/usr/bin/env python3
"""Basic tests for chats app"""
from django.test import TestCase
from .models import User, Conversation, Message

class BasicTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username="testuser", password="pass")
        self.assertEqual(user.username, "testuser")

    def test_conversation_creation(self):
        conv = Conversation.objects.create()
        self.assertIsNotNone(conv.conversation_id)
