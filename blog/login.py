from pyramid.url import route_url
from hashlib import sha512
from pyramid.security import remember
from pyramid.security import forget
from pyramid.httpexceptions import HTTPFound

def login(request):
    login_url = route_url('login', request)
    referer = request.url
    if referer == login_url:
        referer = "/"
    came_from = request.params.get('came_from', referer)
    message = ''
    username = ''
    password = ''
    if 'form.submitted' in request.params:
        username = request.params['username']
        password = request.params['password']
        cur = request.db.Users.find({"username":username,"password":sha512(password).hexdigest()}).limit(1)
        if cur.count() > 0:
            headers = remember(request, username)
            return HTTPFound(location = came_from,
                            headers = headers)
        message = 'Invalid Username and Password combination.'
    
    return dict(
        message = message,
        url = request.application_url + '/login',
        came_from = came_from,
        login = username,
        password = '',
        )

def logout(request):
    headers = forget(request)
    return HTTPFound(location = route_url("home", request), headers = headers)
