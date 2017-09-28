import tornado.web
import tornado.ioloop
from views import index
from views import mine
import config

if __name__ == "__main__":
    app = tornado.web.Application([
        (r'/', index.IndexHandler),
        (r'/mine', mine.MineHandler),
    ], **config.settings)

    # print(config.options["list"])
    app.listen(config.options["port"])
    tornado.ioloop.IOLoop.current().start()
