from .models import *

author= Author.objects.get(name="jules")
books = Books.objects.all()
librarian=Librarian.objects.all()