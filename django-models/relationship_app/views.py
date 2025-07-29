"""Views for relationship_app."""

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from .models import Book, Library


def list_books(request):
    """Function-based view that lists all books."""
    books = Book.objects.select_related('author').all()

    if request.GET.get("format") == "text":
        # Return a plain text list if `?format=text` is passed in the URL
        lines = [f"{book.title} by {book.author.name}" for book in books]
        return HttpResponse("\n".join(lines), content_type="text/plain")
    
    # Default to rendering with template
    return render(request, 'list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    """Display details of a single library and its related books."""

    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"

    def get_queryset(self):
        """Fetch the library along with its books and authors."""
        return Library.objects.prefetch_related("books__author")
