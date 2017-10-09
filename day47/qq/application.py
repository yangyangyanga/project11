from tornado.web import Application

from views import index
import config
from yangMysql import YangMySQL

class Application(Application):
    def __init__(self):
        handlers = [
            # 主页，带有好友列表的界面
            (r'/', index.IndexHandler),

            # 登录界面
            (r'/login', index.LoginHandler),
            # 注册界面
            (r'/register', index.RegisterHandler),

            # 群
            (r'/talk', index.TalkHandler),
            (r'/talkk', index.TalkkHandler),
            # 会话界面
            (r'/message', index.MessageHandler),
            (r'/chat', index.ChatHandler),

        ]
        super(Application, self).__init__(handlers, **config.settings)
        self.db = YangMySQL("10.0.142.250", "root", "sunck", "test")