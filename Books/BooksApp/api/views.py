from django_filters import rest_framework
from django.forms import DateInput
from rest_framework import generics
from .serializers import BookSerializer
from ..models import Book


class BookFilter(rest_framework.FilterSet):
    title = rest_framework.CharFilter(field_name='title', lookup_expr='icontains')
    author = rest_framework.CharFilter(field_name='author', lookup_expr='icontains')
    publish_lang = rest_framework.CharFilter(field_name='publish_lang', lookup_expr='icontains')
    start_date = rest_framework.DateFilter(field_name='publish_date', lookup_expr='gte', widget=DateInput(attrs={'type': 'date'}))
    end_date = rest_framework.DateFilter(field_name='publish_date', lookup_expr='lte', widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Book
        fields = ['title', 'author']


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (rest_framework.DjangoFilterBackend, )
    filterset_class = BookFilter
