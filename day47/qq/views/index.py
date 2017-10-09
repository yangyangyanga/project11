import tornado.web
from tornado.web import RequestHandler
from tornado.websocket import WebSocketHandler

class IndexHandler(RequestHandler):
    users = []
    def get_current_user(self):
        flag = self.get_argument("flag", default=None)
        if flag:
            return True
        else:
            return False
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        fla = True
        for user in self.users:
            if self.request.remote_ip == user:
                fla = False
        if fla:
            self.users.append(self.request.remote_ip)
        print("uu11 -- ", self.users)
        next = self.get_argument("next", "/")
        goodfriendurl = next + "?flag=logined"
        self.render('index/goodfriend.html', title='QQ', goodfriendurl=goodfriendurl,users=self.users)

class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index/login.html', title='登录')
    def post(self, *args, **kwargs):
        username = self.get_body_argument('username')
        password = self.get_body_argument('password')
        print(username+"---"+password)
        userList = self.application.db.get_all_obj("select * from user", "user")
        print(userList)
        for userl in userList:
            if username == userl["username"] and password == userl["password"]:
                next = self.get_argument("next", "/")
                return self.redirect(next+"?flag=logined")

        next = self.get_argument("next", "/")
        return self.redirect('/login?next=' + next)

class RegisterHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index/register.html', title='注册', remain="")
    def post(self, *args, **kwargs):
        username = self.get_body_argument("username")
        password = self.get_body_argument("passwd")
        checkpasswd = self.get_body_argument("checkpasswd")
        smallname = self.get_body_argument("smallname")
        pic = self.request.files
        print(type(pic))
        print(pic)
        userList = self.application.db.get_all_obj("select * from user", "user")
        for userl in userList:
            if username == userl["username"]:
                remain = "账号已存在"
                self.render('index/register.html', title='注册', remain=remain)
            elif password != checkpasswd:
                remain = "密码不一致"
                self.render('index/register.html', title='注册', remain=remain)
        uid = str(len(userList) + 1)
        # print(uid)
        count = self.application.db.insert("insert into user values('%s','%s', '%s', '%s' )"%(uid,username, password, smallname))
        print("----"+str(count)+"------")
        if count:
            self.redirect('/login')
        else:
            self.redirect('/register')

class MessageHandler(RequestHandler):
    users = []
    def get(self, *args, **kwargs):
        # print("me = ", self.request.remote_ip)
        # print("meself = ", self)
        fla = True
        for user in self.users:
            if self.request.remote_ip == user:
                fla = False
        if fla:
            self.users.append(self.request.remote_ip)
        # print("uu -- ", self.users)
        next = self.get_argument("next", "/")
        goodfriendurl = next+"?flag=logined"
        self.render('index/message.html', title='会话', goodfriendurl=goodfriendurl, users=self.users)

class ChatHandler(WebSocketHandler):
    users = []
    def open(self, *args, **kwargs):
        # print(self.request.remote_ip)
        # print("self = ", self)
        self.users.append(self)
        # for user in self.users:
        #     user.write_message(u"[%s]登录了"%(self.request.remote_ip))
            # self.render('index/message.html', users=self.users)
    def on_message(self, message):
        # 发送广播请求
        for user in self.users:
            user.write_message(r'[%s]：%s'%(self.request.remote_ip, message))
    def on_close(self):
        self.users.remove(self)
        # for user in self.users:
        #     user.write_message(r'[%s]下线了'%(self.request.remote_ip))

# 群聊
class TalkHandler(RequestHandler):
    users = []
    def get(self, *args, **kwargs):
        print("me = ", self.request.remote_ip)
        print("meself = ", self)
        fla = True
        for user in self.users:
            if self.request.remote_ip == user:
                fla = False
        if fla:
            self.users.append(self.request.remote_ip)
        print("uu -- ", self.users)
        next = self.get_argument("next", "/")
        goodfriendurl = next + "?flag=logined"
        self.render('index/talk.html', title='群', goodfriendurl=goodfriendurl, users=self.users)

class TalkkHandler(WebSocketHandler):
    users = []
    def open(self, *args, **kwargs):
        print(self.request.remote_ip)
        print("self = ", self)
        self.users.append(self)
    def on_message(self, message):
        # 发送广播请求
        for user in self.users:
            user.write_message(r'[%s]：%s'%(self.request.remote_ip, message))
    def on_close(self):
        self.users.remove(self)
