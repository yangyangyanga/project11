import tornado.web
import tornado.ioloop

from application import Application
import config
if __name__ == "__main__":
    app = Application()
    app.listen(config.options["port"])
    tornado.ioloop.IOLoop.current().start()