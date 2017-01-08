from pyramid.config import Configurator
from .controllers import home_controller

def main(global_config, **settings):
    """
        This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.include('pyramid_handlers')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('make_cv', '/make_cv')
    config.scan()
    return config.make_wsgi_app()
