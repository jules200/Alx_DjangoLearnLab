from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('posts.urls')),
    path('feed/', FeedView.as_view(), name='user-feed'),
    path('api/accounts/', include('accounts.urls')),  # Follow and Unfollow URLs
    path('api/posts/', include('posts.urls')),  
]