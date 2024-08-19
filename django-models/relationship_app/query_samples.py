from .models import *

author= Author.objects.get(name=author_name)
books = Books.objects.filter(author=author)
library=Library.objects.get(name=library_name)
librarian=Librarian.objects.get(library=library_name)

books.all()

# @user_passes_test(lambda u: role_check(u, 'Admin'))
# def role_check(user,role):
#     return user.userprofile.role and user.userprofile.role == role