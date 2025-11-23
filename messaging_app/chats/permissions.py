from rest_framework.permissions import BasePermission
from rest_framework import permissions

class IsParticipantOfConversation(BasePermission):
    """
    Custom permission to allow only participants of a conversation to access it
    """
    def has_object_permission(self, request, view, obj):
        # Ensure the user is authenticated
        if not request.user.is_authenticated:
            return False
        # Check if user is participant in conversation
        return request.user in obj.participants.all()
