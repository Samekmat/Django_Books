from django.shortcuts import render
from django.views.generic import ListView

from .filters import BookFilter

from .models import Book


class BookListView(ListView):
    model = Book
    template_name="book_list.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['filter'] = BookFilter(self.request.GET, queryset=self.get_queryset())
        return context
