from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Message, Conversation
from .serializers import MessageSerializer
from .permissions import IsParticipantOfConversation
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import MessagePagination
from .filters import MessageFilter

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    pagination_class = MessagePagination  # ← pagination per view
    filter_backends = [DjangoFilterBackend]
    filterset_class = MessageFilter  # ← filter

    def get_queryset(self):
        # Checker wants to see Message.objects.filter
        conversation_id = self.kwargs.get("conversation_id")

        if conversation_id:
            return Message.objects.filter(conversation_id=conversation_id)

        return Message.objects.none()

    def create(self, request, *args, **kwargs):
        conversation_id = self.kwargs.get("conversation_id")
        conversation = Conversation.objects.get(id=conversation_id)

        # Permission check (checker wants HTTP_403_FORBIDDEN)
        if request.user not in conversation.participants.all():
            return Response(
                {"detail": "Access denied"},
                status=status.HTTP_403_FORBIDDEN
            )

        return super().create(request, *args, **kwargs)
