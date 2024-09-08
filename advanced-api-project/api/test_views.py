from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book, Author


class BookAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(title="Harry Potter", publication_year=1997, author=self.author)

def test_create_book(self):
    data = {
        "title": "The Hobbit",
        "publication_year": 1937,
        "author": self.author.id
    }
    response = self.client.post(reverse('book-create'), data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Book.objects.count(), 2)
    self.assertEqual(Book.objects.last().title, "The Hobbit")
    
def test_get_books(self):
    response = self.client.get(reverse('book-list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)
    self.assertEqual(response.data[0]['title'], "Harry Potter")
    
def test_get_single_book(self):
    response = self.client.get(reverse('book-detail', kwargs={'pk': self.book.id}))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['title'], "Harry Potter")
    
def test_update_book(self):
    data = {"title": "Harry Potter and the Philosopher's Stone"}
    response = self.client.put(reverse('book-update', kwargs={'pk': self.book.id}), data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.book.refresh_from_db()
    self.assertEqual(self.book.title, "Harry Potter and the Philosopher's Stone")
    
def test_delete_book(self):
    response = self.client.delete(reverse('book-delete', kwargs={'pk': self.book.id}))
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(Book.objects.count(), 0)
    
def test_filter_books_by_title(self):
    response = self.client.get(reverse('book-list') + '?title=Harry Potter')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)
    
def test_search_books_by_author(self):
    response = self.client.get(reverse('book-list') + '?search=Rowling')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)
    
def test_order_books_by_publication_year(self):
    response = self.client.get(reverse('book-list') + '?ordering=publication_year')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    
def test_create_book_without_authentication(self):
    data = {
        "title": "The Hobbit",
        "publication_year": 1937,
        "author": self.author.id
    }
    response = self.client.post(reverse('book-create'), data)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)