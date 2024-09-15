from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.views.generic.edit import UpdateView
from .forms import UserUpdateForm

class UserLoginView(LoginView):
    template_name = 'blog/login.html'
class UserLogoutView(LogoutView):
    template_name = 'blog/logout.html'
    
class UserLogoutView(LogoutView):
    template_name = 'blog/logout.html'
    
class UserRegisterView(CreateView):
    if request.method == "POST":
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