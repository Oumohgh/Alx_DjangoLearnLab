# Delete

```python
from bookshelf.models import Book

# Delete the book
book = Book.objects.get(id=1)  # Replace 1 with your actual book ID
book.delete()

# Confirm deletion
Book.objects.all()
# Output: <QuerySet []>