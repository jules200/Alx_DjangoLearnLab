from .models import *

author= Author.objects.get(name=author_name)
books = Books.objects.filter(author=author)
library=Library.objects.get(name=library_name)
librarian=Librarian.objects.get(library=library_name)

books.all()