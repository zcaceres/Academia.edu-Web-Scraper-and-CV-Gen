import pyramid_handlers
from .base_controller import BaseController

class Home_Controller(BaseController):

    @pyramid_handlers.action(renderer="home.pt")
    def index(self):
        return {}
