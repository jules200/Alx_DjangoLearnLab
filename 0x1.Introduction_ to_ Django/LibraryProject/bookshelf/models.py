from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length="200")
    author = models.CharField(max_length="100")
    publication_year = models.IntegerField()
    
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Book'
        verbose_name_plural = 'Books'