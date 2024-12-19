from rest_framework.pagination import PageNumberPagination


class habitPaginator(PageNumberPagination):
    page_size = 5
