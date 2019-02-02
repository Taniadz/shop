from django import forms
from books.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'ISBN', 'publish_date', 'authors']
        widgets = {
            'publish_date': forms.DateInput(attrs={'class': 'datepicker'}),
        }
