from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from books.forms import BookForm
from books.models import Book


class BookListView(ListView):
    model = Book
    template_name = "book_list.html"


class BookDetailView(DetailView):
    model = Book
    template_name="book_detail.html"


class BookCreateView(CreateView):
    form_class = BookForm
    model = Book
    template_name = 'book_form.html'


class BookUpdateView(UpdateView):
    form_class = BookForm
    model = Book
    template_name = 'book_form.html'


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')
    template_name = 'book_confirm_delete.html'

