import tornado.web
import tornado.ioloop
import tornado.options
import config
class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("sunck is a good man")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r'/', IndexHandler),
    ], **config.settings)
    print(config.options["port"])
    print(config.options["list"])
    app.listen(config.options["port"])
    tornado.ioloop.IOLoop.current().start()
