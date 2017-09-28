import tornado.web
import tornado.ioloop

# 引入httpserver模块
import tornado.httpserver

# 处理类（相当于Django中的视图类）
class IndexHandler(tornado.web.RequestHandler):
    # 一个响应，响应信息
    def get(self, *args, **kwargs):
        self.write("yang yang yang")

if __name__ == "__main__":
    # 一个app实例
    app = tornado.web.Application([
        (r'/', IndexHandler),
    ])
    # app.listen(8000)

    # 实例化一个httpserver对象
    httpServer = tornado.httpserver.HTTPServer(app)
    # 绑定端口
    httpServer.bind(8000)

    # 开启监听
    tornado.ioloop.IOLoop.current().start()