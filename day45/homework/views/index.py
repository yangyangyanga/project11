from tornado.web import RequestHandler

# 首页
class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # 从cookie中取得name值为username的value
        username = self.get_secure_cookie("username")
        # username = self.get_cookie("username", default="游客")
        print(username)
        if username == None:
            h1 = "请登录"
            remain = "登录"
            aurl = self.reverse_url("login")
            username = ""
        else:
            h1 = "欢迎"
            remain = "退出登录"
            aurl = self.reverse_url("quitlogin")
        pers = {
            "h1":h1,
            "username": username,
            "remain": remain,
            "aurl": aurl,
        }
        self.render('index/index.html',title="首页", **pers)
# 登录界面
class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        register_url = self.reverse_url("register")
        logintoindex_url = self.reverse_url("logintoindex")
        pers = {
            "register_url": register_url,
            "logintoindex_url": logintoindex_url,
        }
        self.render("index/login.html", title="登录界面", per=pers)
# 登录提交
class LogintoindexHandler(RequestHandler):
    def post(self, *args, **kwargs):
        # 从登录表单中获取账号、密码
        username = self.get_body_argument("username")
        password = self.get_body_argument("passwd")
        usersList = self.application.db.get_all_obj("select * from user", "user")
        for user in usersList:
            if username == user["username"] and password == user["password"]:
                # 将账号设置到cookie中
                self.set_secure_cookie("username", username)
                # self.set_cookie("username", username)
                self.redirect("/")
            # else:
            #     self.redirect("/login")
        self.redirect("/login")
        # self.render('index/index.html', title="首页", per=pers)
# 退出登录
class QuitloginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.clear_cookie("username", path="/", )
        self.redirect('/')
# 注册界面
class RegisterHandler(RequestHandler):
    def get(self, *args, **kwargs):
        registersuccess_url = self.reverse_url("registersuccess")
        rremain = ""
        self.render("index/register.html", title="注册界面", registersuccess_url=registersuccess_url, rremain=rremain)

class RegisterSuccessHandler(RequestHandler):
    def post(self, *args, **kwargs):
        rusername = self.get_body_argument("username")
        rpasswd = self.get_body_argument("passwd")
        rcheckpasswd = self.get_body_argument("checkpasswd")
        rsmallname = self.get_body_argument("smallname")
        # print(rusername)
        # print(rpasswd)
        # print(rcheckpasswd)
        # print(rsmallname)
        userList = self.application.db.get_all_obj("select * from user", "user")
        # print(userList)
        # rremain = ""
        registersuccess_url = self.reverse_url("registersuccess")
        ap = self.application
        for peruser in userList:
            if rusername == peruser["username"]:
                rremain = "已有该账号"
                self.render('index/register.html',title="注册界面", registersuccess_url=registersuccess_url,rremain=rremain)
            elif rpasswd != rcheckpasswd:
                rremain = "密码验证不对"
                self.render('index/register.html',title="注册界面", registersuccess_url=registersuccess_url,rremain=rremain)
            else:
                count = str(len(userList) + 1)
                print("count = ", count)
                c = self.application.db.insert("insert into user values(%s,%s, %s, %s)"%(count,rusername, rpasswd, rsmallname))
                # c = ap.db.insert("insert into user values(" +count + rusername + rpasswd + rsmallname+")")
                # c = ap.db.insert("insert into user values('4', 'yyx', '123', 'yyx1')")

                # print("xiugai = ", self.application.db.get_all_obj("select * from user", "user"))
                print("c = ", c)
                # if c == 1:
                #     self.redirect('/')
                # else:
                #     self.redirect('/register')

        # self.render('index/register.html', title="注册界面",registersuccess_url=registersuccess_url,rremain=rremain)
