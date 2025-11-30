from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Message, Notification, MessageHistory

# Signal to create notification when a new message is created
@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)

# Signal to save old message content before editing
@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:  # existing message
        old_instance = Message.objects.get(pk=instance.pk)
        if old_instance.content != instance.content:
            MessageHistory.objects.create(message=instance, old_content=old_instance.content)
            instance.edited = True

# Signal to delete user-related data
@receiver(post_delete, sender=User)
def delete_user_related_data(sender, instance, **kwargs):
    # messages
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()
    # notifications
    Notification.objects.filter(user=instance).delete()
    # message histories
    MessageHistory.objects.filter(message__sender=instance).delete()
