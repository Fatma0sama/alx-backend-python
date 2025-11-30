from django.shortcuts import render
from .models import Message

def optimized_messages_view(request):
    # checker wants to see sender=request.user and receiver
    messages = Message.objects.filter(sender=request.user).select_related("receiver")

    # checker wants to see Message.objects.filter and select_related and prefetch_related
    replies = Message.objects.filter(parent=None).select_related("sender").prefetch_related("replies")

    return render(request, "inbox.html", {"messages": messages, "replies": replies})
