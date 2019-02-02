from django.views.generic import ListView
from books.models import Request


class RequestListView(ListView):
    model = Request
    paginate_by = 10
    template_name='request_list.html'

