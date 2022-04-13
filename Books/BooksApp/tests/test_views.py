from django.test import TestCase, Client
from django.urls import reverse
from BooksApp.models import Book 
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-page', args=[1])
        self.create_url = reverse('book-create')
        self.delete_url = reverse('book-delete', args=[1])
        self.update_url = reverse('book-update', args=[1])
        self.index_url = reverse('index')
        self.import_url = reverse('book-import')
        self.book1 = Book.objects.create(
            title='test',
            author='test',
            publish_date='04-04-2020',
            isbn='9783161484100',
            page_num='560',
            cover_link='https://www.google.com/',
            publish_lang='en'
            )

### GET ###

    def test_book_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_list.html')
    
    def test_book_detail_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_detail.html')

    def test_book_create_GET(self):
        response = self.client.get(self.create_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_form.html')
    
    def test_book_delete_GET(self):
        response = self.client.get(self.delete_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_delete.html')
    
    def test_book_update_GET(self):
        response = self.client.get(self.update_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_form.html')
    
    def test_index_GET(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_book_import_GET(self):
        response = self.client.get(self.import_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_import.html')

    def test_api_GET(self):
        response = self.client.get('/api/')
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response)

    def test_book_detail_not_existing(self):
        response = self.client.get(reverse('book-page', args=[1076876]))

        self.assertEquals(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')

### POST ###

    def test_book_create_POST(self):
        response = self.client.post(self.create_url, {
            'title': 'test1',
            'author': 'me',
           'publish_date': '04-04-2020',
            'isbn': '9783161484100',
            'page_num': '560',
            'cover_link': 'https://www.google.com/',
            'publish_lang': 'en'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Book.objects.all().count(), 2)
        self.assertEquals(Book.objects.all()[1].author, 'me')

    def test_book_create_POST_no_data(self):
        response = self.client.post(self.create_url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(Book.objects.all().count(), 1)

### DELETE ###

    def test_book_delete_DELETE(self):
        Book.objects.create(
            title='to_delete',
            author='deltest',
            publish_date='03-03-2020',
            isbn='9783161484100',
            page_num='50',
            cover_link='https://www.google.com/',
            publish_lang='pl'
            )

        response = self.client.delete(self.delete_url, json.dumps({
            'id': 2
        }))

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Book.objects.all().count(), 1)

    def test_book_delete_DELETE_no_id(self):
        Book.objects.create(
            title='to_delete',
            author='deltest',
            publish_date='03-03-2020',
            isbn='9783161484100',
            page_num='50',
            cover_link='https://www.google.com/',
            publish_lang='pl'
            )

        response = self.client.delete(self.delete_url)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Book.objects.all().count(), 1)