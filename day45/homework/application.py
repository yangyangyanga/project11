from tornado.web import Application
import tornado.web
import config
from views import index
from yangMysql import YangMySQL

class Application(Application):
    def __init__(self):
        handler = [
            (r'/', index.IndexHandler),
            tornado.web.url(r'/login', index.LoginHandler, name="login"),
            tornado.web.url(r'/logintoindex', index.LogintoindexHandler, name="logintoindex"),
            tornado.web.url(r'/quitlogin', index.QuitloginHandler, name="quitlogin"),

            tornado.web.url(r'/register', index.RegisterHandler, name="register"),
            tornado.web.url(r'/registersuccess', index.RegisterSuccessHandler, name="registersuccess"),
        ]
        super(Application, self).__init__(handler, **config.settings)
        # 连接数据库对象
        self.db = YangMySQL("10.0.142.250", "root", "sunck", "test")