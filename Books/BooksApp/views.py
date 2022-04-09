from re import template
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView

from .forms import BookForm

from .filters import BookFilter

from .models import Book


class BookListView(ListView):
    model = Book
    template_name="book_list.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['filter'] = BookFilter(self.request.GET, queryset=self.get_queryset())
        return context


class BookCreateView(CreateView):
    form_class = BookForm
    template_name = 'book_form.html'

    def get_success_url(self):
        return reverse('book-list')
