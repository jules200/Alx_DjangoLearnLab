from .models import *

author= Author.objects.get(name="jules")
books = Books.objects.all()
librarian=Librarian.objects.get(name=library_name)

books.all()