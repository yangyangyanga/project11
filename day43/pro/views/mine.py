import tornado.web
from tornado.web import RequestHandler

class MineHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("sunck is a nice man")

