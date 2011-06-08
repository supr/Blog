from pyramid.security import Allow
from pyramid.security import Everyone

class Root(object):
    __acl__ = [ (Allow, Everyone, 'view'),
                (Allow, 'admins', ('new', 'edit')),
                ]
    def __init__(self, request):
        self.request = request
