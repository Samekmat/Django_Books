from re import template
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, DetailView, ListView

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
        return reverse('book-page')


class BookDetailView(DetailView):
    template_name = 'book_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Book, id=id_)


class BookDeleteView(DeleteView):
    template_name = 'book_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Book, id=id_)

    def get_success_url(self):
        return reverse('book-list')
