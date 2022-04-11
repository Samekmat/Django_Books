from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import BookForm
from .filters import BookFilter
from .models import Book

import requests


def index(request):
    return render(request, 'index.html')


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
        return reverse('book-page', args=(self.object.id, ))


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


class BookUpdateView(UpdateView):
    template_name = 'book_form.html'
    form_class = BookForm

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Book, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('book-list')


def books_import(request):
    bulk_list = []
    url = f'https://www.googleapis.com/books/v1/volumes?q='

    if 'queryS' in request.GET:
        query = request.GET['queryS']
        url += query
        if 'titleS' in request.GET:
            title_s = request.GET['titleS']
            if title_s != '':
                url += f'+intitle:{title_s}'
        if 'authorS' in request.GET:
            author_s = request.GET['authorS']
            if author_s != '':
                url += f'+inauthor:{author_s}'
        if 'isbnS' in request.GET:
            isbn_s = request.GET['isbnS']
            if isbn_s != '':
                url += f'+isbn:{isbn_s}'

        if 'publisherS' in request.GET:
            publisher_s = request.GET['publisherS']
            if publisher_s != '':
                url += f'+inpublisher:{publisher_s}'

        if 'subjectS' in request.GET:
            subject_s = request.GET['subjectS']
            if subject_s != '':
                url += f'+subject:{subject_s}'

        if 'lccnS' in request.GET:
            lccn_s = request.GET['lccnS']
            if lccn_s != '':
                url += f'+lccn:{lccn_s}'

        if 'oclcS' in request.GET:
            oclc_s = request.GET['oclcS']
            if oclc_s != '':
                url += f'+isbn:{oclc_s}'

        response = requests.get(url)
        data = response.json()
        books_info = data['items']

        for book in books_info:
            try:

                if book['volumeInfo']['title']:
                    title = book['volumeInfo']['title']

                if book['volumeInfo']['authors']:
                    author = book['volumeInfo']['authors']

                if book['volumeInfo']['publishedDate']:
                    date = book['volumeInfo']['publishedDate']

                if book['volumeInfo']['industryIdentifiers']:
                    identifiers = book['volumeInfo']['industryIdentifiers']

                    for num in identifiers:
                        if num['type'] == 'ISBN_10' or num['type'] == 'ISBN_13':
                            isbn = num['identifier']
                        else:
                            isbn = None

                if book['volumeInfo']['pageCount']:
                    page_num = book['volumeInfo']['pageCount']

                if book['volumeInfo']['imageLinks']['thumbnail']:
                    cover_link = book['volumeInfo']['imageLinks']['thumbnail']

                if book['volumeInfo']['language']:
                    publish_lang = book['volumeInfo']['language']

                book_data = Book(
                    title=title,
                    author=author,
                    publish_date=date,
                    isbn=isbn,
                    page_num=page_num,
                    cover_link=cover_link,
                    publish_lang=publish_lang
                )

                bulk_list.append(book_data)

            except Exception as e:
                print(e)

        Book.objects.bulk_create(bulk_list)

    return render(request, 'book_import.html',
        {'books_found': Book.objects.all().order_by('-id')})
