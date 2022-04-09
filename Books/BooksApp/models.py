from django.db import models
from isbn_field import ISBNField


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publish_date = models.DateField(null=True)
    isbn = ISBNField()
    page_num = models.IntegerField(null=True)
    cover_link = models.URLField(blank=True)
    publish_lang = models.CharField(max_length=64)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title
