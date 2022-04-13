from django.test import SimpleTestCase
from django.urls import reverse, resolve
from BooksApp.views import (
    BookCreateView,
    BookDeleteView,
    BookDetailView,
    BookListView,
    BookUpdateView,
    books_import,
    index,
)


class TestUrls(SimpleTestCase):

    def test_book_create_url_is_resolves(self):
        url = reverse('book-create')
        self.assertEquals(resolve(url).func.view_class, BookCreateView)


    def test_book_delete_url_is_resolves(self):
        url = reverse('book-delete', args=[1])
        self.assertEquals(resolve(url).func.view_class, BookDeleteView)

    def test_book_page_url_is_resolves(self):
        url = reverse('book-page', args=[1])
        self.assertEquals(resolve(url).func.view_class, BookDetailView)

    def test_book_list_url_is_resolves(self):
        url = reverse('book-list')
        self.assertEquals(resolve(url).func.view_class, BookListView)
    
    def test_book_update_url_is_resolves(self):
        url = reverse('book-update', args=[1])
        self.assertEquals(resolve(url).func.view_class, BookUpdateView)

    def test_book_import_url_is_resolves(self):
        url = reverse('book-import')
        self.assertEquals(resolve(url).func, books_import)

    def test_index_url_is_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)
