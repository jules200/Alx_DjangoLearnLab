from django.db import models

# Create your models here.

ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member')
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, null=False, on_delete=models.CASCADE)
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        
class Library(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book, null=False)
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Library'
        verbose_name_plural = 'Librarys'
        
class Librarian(models.Model):
    name = models.CharField(max_length=50)
    library = models.OneToOneField(Library, null=False,  on_delete=models.CASCADE)