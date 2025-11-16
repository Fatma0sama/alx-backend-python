#!/usr/bin/env python3
"""Serializers for messaging app"""
from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""

    class Meta:
        model = User
        fields = ["user_id", "first_name", "last_name", "email", "phone_number", "role"]


class MessageSerializer(serializers.ModelSerializer):
    """Serializer for Message model"""
    sender = serializers.CharField(source="sender.email", read_only=True)

    class Meta:
        model = Message
        fields = ["message_id", "sender", "message_body", "sent_at"]


class ConversationSerializer(serializers.ModelSerializer):
    """Serializer for Conversation model"""
    participants = UserSerializer(many=True, read_only=True)
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ["conversation_id", "participants", "messages", "created_at"]

    def get_messages(self, obj):
        """Return messages for the conversation"""
        messages = obj.messages.all()
        return MessageSerializer(messages, many=True).data

    def validate(self, data):
        """Example validation using ValidationError"""
        if not data:
            raise serializers.ValidationError("No data provided")
        return data
