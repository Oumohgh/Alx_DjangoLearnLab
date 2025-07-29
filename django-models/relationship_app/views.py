"""Views for relationship_app."""

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView

from .models import Book, Library


def list_books(request):
    """Function-based view returning a plain-text list of books."""
    books = Book.objects.select_related("author").all()
    lines = [f"{book.title} by {book.author.name}" for book in books]
    # The content type is text/plain so the output is a simple text list as
    # required by the task instructions.
    return HttpResponse("\n".join(lines), content_type="text/plain")


class LibraryDetailView(DetailView):
    """Display details of a single library and its related books."""

    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"

    def get_queryset(self):
        """Fetch the library along with its books and authors."""
        return Library.objects.prefetch_related("books__author")
