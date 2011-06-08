from pyramid.view import view_config

@view_config( route_name = "home", renderer = "index.mk" )
def home(request):
    return { 'title':'Welcome'}

@view_config( route_name = "new", renderer = "new.mk", permission = "new" )
def new_entry(request):
    return {}
