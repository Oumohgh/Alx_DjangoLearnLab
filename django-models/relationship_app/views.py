from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from .models import Book, Library


def list_books(request):
    """Function-based view that lists all books."""
    books = Book.objects.select_related('author').all()
    return render(request, 'list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    """Display details of a single library and its books."""
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
