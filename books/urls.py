from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name="book_detail"),
    path('book/add', views.BookCreateView.as_view(),  name="book_add"),
    path('book/edit/<int:pk>', views.BookUpdateView.as_view(), name="book_edit"),
    path('book/delete/<int:pk>', views.BookDeleteView.as_view(), name="book_delete"),
    path('requests', views.RequestListView.as_view()),

]

