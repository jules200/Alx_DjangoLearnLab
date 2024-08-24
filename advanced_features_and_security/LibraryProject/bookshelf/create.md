from .models import Book

# Create a new Book instance
book = Book.objects.create(title="My First Book", author="George Orwell", published_year="1984")

# Save the instance (if not using .create())
# book.save()

print(f"Created Book: {book}")