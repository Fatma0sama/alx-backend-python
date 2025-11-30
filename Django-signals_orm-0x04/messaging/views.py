from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Message

@cache_page(60)
def inbox(request):
    user = request.user
    messages = Message.unread.for_user(user).select_related('sender').prefetch_related('replies')
    return render(request, 'messaging/inbox.html', {'messages': messages})
