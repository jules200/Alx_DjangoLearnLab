from .import views

urlspattern=[
    path('bookslist', views.bookslist, name='bookslist'),
]