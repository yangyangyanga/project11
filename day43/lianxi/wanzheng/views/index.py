from tornado.web import RequestHandler

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hahahhahaha......")