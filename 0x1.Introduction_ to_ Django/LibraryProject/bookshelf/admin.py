from django.contrib import admin
from .models import Book
# Register your models here.
@admin_register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('list_filter', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')
    