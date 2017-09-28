import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

tornado.options.define("port", default=8000, type=int, help="this is port", multiple=False)
tornado.options.define("list", default=[], type=str, help="this is port", multiple=False)

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("yangyangyang")

if __name__  == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r'/', IndexHandler)
    ])

    print(tornado.options.options.port)
    app.listen(tornado.options.options.port)

    tornado.ioloop.IOLoop.current().start()
