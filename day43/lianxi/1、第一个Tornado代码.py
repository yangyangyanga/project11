import tornado.web
import tornado.ioloop

# 处理类（相当于Django中的类视图）
class IndexHandeler(tornado.web.RequestHandler):
    # 路由处理方法（匹配路由执行）
    def get(self, *args, **kwargs):
        # 一个响应，响应信息
        self.write("sunck is a good man")

if __name__ == "__main__":
    # 创建一个app实例（一个应用）
    # Application:  Tornado web的
    app = tornado.web.Application([
        (r'/', IndexHandeler)
    ])
    # 绑定监听的端口，注意：此时也没有开启监听
    app.listen(8000)
    # IOLoop.current(): 返回当前线程的IOLoop实例
    # IOLoop.start():   开启
    tornado.ioloop.IOLoop.current().start()