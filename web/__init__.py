from pyramid.config import Configurator
from pyramid.response import Response
from .models import Note, Session, Base, engine
from pyramid.session import SignedCookieSessionFactory


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        my_session_factory = SignedCookieSessionFactory('itsaseekreet')
        config.set_session_factory(my_session_factory)
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.scan()
    return config.make_wsgi_app()
