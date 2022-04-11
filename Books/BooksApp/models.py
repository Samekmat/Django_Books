from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publish_date = models.CharField(max_length=40, null=True)
    isbn = models.IntegerField(null=True, blank=True)
    page_num = models.IntegerField(null=True)
    cover_link = models.URLField(blank=True)
    publish_lang = models.CharField(max_length=64)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title
