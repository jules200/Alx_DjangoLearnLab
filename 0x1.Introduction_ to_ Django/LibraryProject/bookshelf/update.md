from .models import Book


retrieved_book.title = "My Updated Book Title"
retrieved_book.save()

print(f"Updated Book: {retrieved_book}")