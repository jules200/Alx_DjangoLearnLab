from .models import Book


books = Book.object.get(published_year="1984")


print(books)