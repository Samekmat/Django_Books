from django.contrib import admin
from django.urls import path
from BooksApp.models import Book

from BooksApp.views import BookCreateView, BookListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookListView.as_view(), name="book-list" ),
    path('books/add/', BookCreateView.as_view(), name="book-create"),
]
