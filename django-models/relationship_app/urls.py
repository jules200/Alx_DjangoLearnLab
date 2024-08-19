from .views import list_books

urlspattern=[
    path('bookslist', views.bookslist, name='bookslist'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
    path('login/', views.LoginView.as_view(template_name=""), name='login'),
    path('logout/', views.LogoutView.as_view(template_name=""), name='logout'),
    path('register/', views.register, name='register'),
    path('admin-view/', views.admin_view, name='admin-view'),
]