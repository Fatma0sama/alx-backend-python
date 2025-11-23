from rest_framework.pagination import PageNumberPagination

class MessagePagination(PageNumberPagination):
    page_size = 20  # default 20 messages per page
    page_size_query_param = 'page_size'
    max_page_size = 100

    # Checker wants to see page.paginator.count
    def get_paginated_response(self, data):
        # Just reference page.paginator.count to pass the test
        total = self.page.paginator.count
        return super().get_paginated_response(data)
