from .models import Book


books = Book.objects.get(published_year="1984")


print(books)