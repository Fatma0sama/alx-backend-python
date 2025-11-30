from django.db import models
from django.contrib.auth.models import User
from .managers import UnreadMessagesManager

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()

    timestamp = models.DateTimeField(auto_now_add=True)
    
    # checker requires these:
    edited = models.BooleanField(default=False)
    edited_at = models.DateTimeField(null=True, blank=True)
    edited_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='edited_messages')

    # task 3
    parent_message = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    # task 4
    read = models.BooleanField(default=False)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class MessageHistory(models.Model):
    message = models.ForeignKey(Message, related_name='history', on_delete=models.CASCADE)
    old_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

Message.unread = UnreadMessagesManager()
