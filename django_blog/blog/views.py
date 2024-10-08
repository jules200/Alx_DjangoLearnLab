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
from django.contrib.auth.decorators import login_required
from django.db.models import Q

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
    
@login_required
def CommentCreateView(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form})

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/edit_comment.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/delete_comment.html'

    def get_success_url(self):
        post = self.get_object().post
        return reverse_lazy('post-detail', kwargs={'pk': post.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
def search(request):
    query = request.GET.get('q')
    results = Post.objects.filter(
        Q(title__icontains=query) | 
        Q(content__icontains=query) |
        Q(tags__name__icontains=query)  # If using django-taggit
    ).distinct()
    
    return render(request, 'blog/search_results.html', {'results': results, 'query': query})