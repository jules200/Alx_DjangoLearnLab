from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

class Book(models.Model):
    title = models.CharField()
    Author = models.ForeignKey(Author, null=False, on_delete="CASCADE")
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        
class Library(models.Model):
    name = models.CharField()
    books = models.ManyToManyField(Book, null=False)
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Library'
        verbose_name_plural = 'Librarys'
        
class librarian(models.Model):
    name = models.CharField()
    library = models.OneToOneField(Library, null=False)