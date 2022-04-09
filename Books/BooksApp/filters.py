from django_filters import DateFilter, CharFilter, FilterSet
from .models import Book


class BookFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    author = CharFilter(field_name='author', lookup_expr='icontains')
    publish_lang = CharFilter(field_name='publish_lang', lookup_expr='icontains')
    start_date = DateFilter(field_name='publish_date', lookup_expr='gte')
    end_date = DateFilter(field_name='publish_date', lookup_expr='lte')

    class Meta:
        model = Book
        fields = ['title', 'author']
