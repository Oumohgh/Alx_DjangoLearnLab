# CRUD Operations for the Book Model

This document contains the Create, Retrieve, Update, and Delete operations performed on the `Book` model in Django.

---

## 📝 Create

```python
from bookshelf.models import Book

# Create
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
print(book)
# Output: 1984 by George Orwell (1949)
