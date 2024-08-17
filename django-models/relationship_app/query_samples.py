from .models import *

author= Author.objects.get(name=author_name)
authors= Author.objects.filter(name=author)
books = Books.objects.all()
librarian=Library.objects.get(name=library_name)

books.all()