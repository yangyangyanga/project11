import tornado.web
import tornado.ioloop

from views import index
import config

if __name__ == "__main__":
    app = tornado.web.Application([
        (r'/', index.IndexHandler),
    ])

    app.listen(config.options["port"])
    tornado.ioloop.IOLoop.current().start()