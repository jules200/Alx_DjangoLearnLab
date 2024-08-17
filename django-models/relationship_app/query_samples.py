from .models import *

author= Author.objects.get(name=author_name)
books = Books.objects.filter(author=author)
librarian=Library.objects.get(name=library_name)

books.all()