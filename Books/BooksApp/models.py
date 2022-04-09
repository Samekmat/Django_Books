from django.db import models
from isbn_field import ISBNField


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publish_date = models.DateField()
    isbn = ISBNField()
    page_num = models.IntegerField()
    cover_link = models.URLField()
    publish_lang = models.CharField(max_length=64)
