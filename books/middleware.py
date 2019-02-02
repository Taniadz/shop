from books.models import Request


class WriteRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        data = request.__dict__
        Request.objects.create(method=data.get("method"),
                               path=data.get("path"),
                               content_type=data.get("path"),
                               host=data['META']['HTTP_HOST'],
                               user_agent=data['META']['HTTP_USER_AGENT'])
        response = self.get_response(request)
        return response
