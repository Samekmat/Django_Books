from django.test import SimpleTestCase
from BooksApp.forms import BookForm


class TestForms(SimpleTestCase):

    def test_book_form_valid_data(self):
        form = BookForm(data={
            'title': 'test',
            'author': 'test_author',
           'publish_date': '03-01-2021',
            'isbn': '9783161484100',
            'page_num': '56',
            'cover_link': 'https://www.google.com/',
            'publish_lang': 'es'
        })

        self.assertTrue(form.is_valid())

    def test_book_form_no_data(self):
        form = BookForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)