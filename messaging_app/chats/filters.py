import django_filters
from .models import Message

class MessageFilter(django_filters.FilterSet):
    participant = django_filters.NumberFilter(field_name='conversation__participants__id')
    start_date = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    end_date = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Message
        fields = ['participant', 'start_date', 'end_date']
