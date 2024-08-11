from django.contrib import admin
from .models import Book
# Register your models here.
@admin_register(Book)
class BookAdmin(admin.ModelAdmin):
    pass