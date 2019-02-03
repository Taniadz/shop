from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from books.forms import BookForm
from books.models import Book


class BookListView(ListView):
    model = Book
    template_name = "book_list.html"


class BookDetailView(DetailView):
    model = Book
    template_name="book_detail.html"


@method_decorator(staff_member_required, name='dispatch')
class BookCreateView(CreateView):
    form_class = BookForm
    model = Book
    template_name = 'book_form.html'


@method_decorator(staff_member_required, name='dispatch')
class BookUpdateView(UpdateView):
    form_class = BookForm
    model = Book
    template_name = 'book_form.html'


@method_decorator(staff_member_required, name='dispatch')
class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')
    template_name = 'book_confirm_delete.html'

