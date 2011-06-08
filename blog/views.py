from pyramid.view import view_config
from pymongo import DESCENDING
from pyramid.security import authenticated_userid
from datetime import datetime

@view_config( route_name = "home", renderer = "index.mk" )
def home(request):
    entries = request.db.Entries.find({},sort=[("datetime",DESCENDING)]).limit(4)
    return { 'entries':entries }

@view_config( route_name = "new", renderer = "new.mk", permission = "new" )
def new_entry(request):
    message = ''
    if 'form.submitted' in request.params:
        try:
            title = request.params['title']
            content = request.params['content']
            tags = [ x.strip() for x in request.params['tags'].split(",") ]
            username = authenticated_userid(request)
            entry = dict(
                title = title,
                content = content,
                tags = tags,
                username = username,
                datetime = datetime.now(),
                )
            request.db.Entries.insert(entry)
        except:
            message = 'Invalid forum parameters'
            return dict(
                message = message
                )
    return {}
