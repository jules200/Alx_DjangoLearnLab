from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout
from .models import Library
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import permission_required, login_required, user_passes_test

# Create your views here.
def role_check(user, role):
    return user.userprofile.role == role

@user_passes_test(role_check(user, "Admin"))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

def bookslist(request):
    books = Book.objects.all()
    
    return render(request, "relationship_app/list_books.html")

@permission_required(relationship_app.can_add_book)
@user_passes_test(Admin)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context
@user_passes_test(Admin)
@permission_required('relationship_app.can_add_book')
@permission_required('relationship_app.can_change_book')
@permission_required('relationship_app.can_delete_book')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book-list')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

class LoginView(LoginView):
    template_name = 'relationship_app/login.html'

class LogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
    next_page = reverse_lazy('login')