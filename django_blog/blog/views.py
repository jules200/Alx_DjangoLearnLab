from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.views.generic.edit import UpdateView
from .forms import UserUpdateForm
from .models import Post
from .forms import PostForm

class UserLoginView(LoginView):
    template_name = 'blog/login.html'
class UserLogoutView(LogoutView):
    template_name = 'blog/logout.html'
    
class UserLogoutView(LogoutView):
    template_name = 'blog/logout.html'
    
class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')
    
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/profile.html'
    
class ProfileEditView(LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    template_name = 'blog/profile_edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

def profile_edit_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after a successful update
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'blog/profile_edit.html', {'form': form})

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # template to render
    context_object_name = 'posts'  # object name to access in template
    ordering = ['-published_date']  # latest posts first

# DetailView to show individual blog posts
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # template for detail

# CreateView to allow authenticated users to create new posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'  # form template

    # Set the author to the currently logged-in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# UpdateView to enable post authors to edit their posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    # Ensure only the post author can edit the post
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# DeleteView to let authors delete their posts
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')  # Redirect to the list of posts after deletion

    # Ensure only the post author can delete the post
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author