import pyramid_handlers


class BaseController():
    def __init__(self, request):
        print("Initiating base controller")
        self.request = request
