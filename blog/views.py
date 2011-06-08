from pyramid.view import view_config
from pymongo import DESCENDING

@view_config( route_name = "home", renderer = "index.mk" )
def home(request):
    entries = request.db.Entries.find({},sort=[("datetime",DESCENDING)]).limit(4)
    return { 'entries':entries }

@view_config( route_name = "new", renderer = "new.mk", permission = "new" )
def new_entry(request):
    return {}
