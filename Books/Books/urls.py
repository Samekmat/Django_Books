from django.contrib import admin
from django.urls import path

from BooksApp.views import BookCreateView, BookDeleteView, BookDetailView, BookListView, BookUpdateView,\
 books_import, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookListView.as_view(), name="book-list" ),
    path('books/add/', BookCreateView.as_view(), name="book-create"),
    path('books/<int:pk>/', BookDetailView.as_view(), name="book-page"),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name="book-delete"),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name="book-update"),
    path('', index, name="index"),
    path('books/import/', books_import, name="book-import"),
]
