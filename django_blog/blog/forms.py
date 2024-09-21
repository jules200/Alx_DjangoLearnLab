from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from .models import Comment

class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)
    class Meta:
        model = Post
        fields = ['title', 'content']  # Fields for title and content
        widgets = {
            'tags': TagWidget(),  # Optional: A nicer tag input widget
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Only content is editable