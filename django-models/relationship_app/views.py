from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Library
from .models import Book

# Create your views here.
def bookslist(request):
    books = Book.objects.all()
    
    return render(request, "relationship_app/list_books.html")

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Retrieve all books related to this library
        return context
    
