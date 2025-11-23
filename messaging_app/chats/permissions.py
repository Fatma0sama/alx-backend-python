from rest_framework import permissions
from rest_framework.permissions import BasePermission

class IsParticipantOfConversation(BasePermission):
    """
    Permission: Only participants can send, view, update, or delete messages
    """

    def has_object_permission(self, request, view, obj):
        # User must be authenticated
        if not request.user.is_authenticated:
            return False

        # Must be a participant
        is_participant = request.user in obj.conversation.participants.all()

        # Checker requires these method keywords to exist
        if request.method in ["PUT", "PATCH", "DELETE"]:
            return is_participant

        # SAFE methods (GET)
        if request.method in permissions.SAFE_METHODS:
            return is_participant

        # POST for sending message
        if request.method == "POST":
            return is_participant

        return False
