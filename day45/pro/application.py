import tornado.web
import config
import os

from tornado.web import url
from views import index
from sunckMysql import SunckMySQL

from tornado.web import StaticFileHandler

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            # 路由，传参
            (r'/', index.IndexHandler),
            (r'/sunck', index.SunckHandler),
            (r'/kaige', index.KaigeHandler),
            (r'/kaishen', index.KaishenHandler),
            (r'/kaikai', index.KaikaiHandler),
            (r'/kaihuang', index.KaihuangHandler),

            (r'/students', index.StudentsHandler),

            # cookie
            (r'/commoncookie', index.CommoncookieHandler),
            (r'/safecookie', index.SafecookieHandler),

            (r'/(.*)$', StaticFileHandler, {"path": os.path.join(config.BASE_PATH, "static/index/html"), "default_filename": "index.html"})


        ]
        super(Application, self).__init__(handlers, **config.settings)
        self.db = SunckMySQL("10.0.142.250", "root", "sunck", "test")

