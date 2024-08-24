from django.contrib import admin
from .models import Book
# Register your models here.
@admin.site.register(CustomUser, CustomUserAdmin)
class AdminCustomUser(admin.ModelAdmin):
    pass
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('list_filter', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')
    