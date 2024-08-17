from .views import list_books

urlspattern=[
    path('bookslist', views.bookslist, name='bookslist'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
]