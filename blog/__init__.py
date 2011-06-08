from pyramid.config import Configurator
from blog.resources import Root
from pyramid.mako_templating import renderer_factory as mako_factory
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from blog.security import groupfinder
from pyramid.events import NewRequest
import pymongo

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=Root, settings=settings,
                          authentication_policy = AuthTktAuthenticationPolicy(settings['secret'], callback = groupfinder),
                          authorization_policy = ACLAuthorizationPolicy())
    db_uri = settings['db_uri']
    conn = pymongo.Connection(db_uri)
    config.registry.settings['db_conn'] = conn
    config.add_subscriber(add_mongo_db, NewRequest)
    config.add_renderer(".mk", mako_factory)
    config.add_static_view('static', 'blog:static')
    config.add_route('login', '/login',
                     view = 'blog.login.login',
                     view_renderer = 'blog:templates/login.mk')
    config.add_route('logout', '/logout',
                     view = 'blog.login.logout')
    config.add_view('blog.login.login',
                    renderer = 'blog:templates/login.mk',
                    context = 'pyramid.exceptions.Forbidden')
    config.add_route("home", "/")
    config.add_route("new","/new")
    config.scan('blog.views')

    
    return config.make_wsgi_app()

def add_mongo_db(event):
    settings = event.request.registry.settings
    db = settings['db_conn'][settings['db_name']]
    event.request.db = db
