from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member')
    ]
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
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]
        
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