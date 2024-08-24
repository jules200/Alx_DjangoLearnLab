from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm

# Create your views here.
@permission_required("bookshelf.can_insert", raise_exception=True)
def book_list():
    pass

def books():
    pass
