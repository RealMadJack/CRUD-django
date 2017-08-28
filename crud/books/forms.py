from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'pub_date', 'author', 'price', 'pages', 'book_type', )
