import tornado.web
import tornado.ioloop
import tornado.options

tornado.options.define("port", default=8000, type=int, help="this is port", multiple=False)
tornado.options.define("list", default=[], type=str, help="this is port", multiple=True)

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("yangyangyang11")

if __name__  == "__main__":
    tornado.options.parse_config_file("./config")
    app = tornado.web.Application([
        (r'/', IndexHandler)
    ])

    print(tornado.options.options.port)
    print(tornado.options.options.list)
    app.listen(tornado.options.options.port)

    tornado.ioloop.IOLoop.current().start()
