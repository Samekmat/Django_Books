from django_filters import CharFilter, DateFilter, FilterSet
from .models import Book
from django.forms import DateInput


class BookFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    author = CharFilter(field_name='author', lookup_expr='icontains')
    publish_lang = CharFilter(field_name='publish_lang', lookup_expr='icontains')
    start_date = DateFilter(field_name='publish_date', lookup_expr='gte', widget=DateInput(attrs={'type': 'date'}))
    end_date = DateFilter(field_name='publish_date', lookup_expr='lte', widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Book
        fields = ['title', 'author']
