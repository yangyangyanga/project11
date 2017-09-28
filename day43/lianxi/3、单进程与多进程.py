import tornado.web
import tornado.ioloop
from tornado.web import RequestHandler
import tornado.httpserver

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("yang is happy")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r'/', IndexHandler),
    ])
    # app.listen(8080)
    server = tornado.httpserver.HTTPServer(app)
    server.bind(8080)
    server.start(1)

    tornado.ioloop.IOLoop.current().start()