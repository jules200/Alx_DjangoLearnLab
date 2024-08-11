from .models import Book


books = Book.object.all()


print(books)