from tornado.web import Application

from views import index
import config

class Application(Application):
    def __init__(self):
        handler = [
            (r'/', index.IndexHandler),
            (r'/postfile', index.PostfileHandler),
            (r'/setxsrfcookie', index.SetXsrfCookieHandler),
            (r'/ajaxtest', index.AjaxTestHandler),

        ]
        super(Application, self).__init__(handler, **config.settings)