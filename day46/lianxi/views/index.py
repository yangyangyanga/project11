from tornado.web import RequestHandler

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        cookie = self.get_secure_cookie("count")
        if cookie:
            count = int(cookie) + 1
        else:
            count = 1
        self.set_secure_cookie("count", str(count))
        self.render('index/index.html', count=count)

class PostfileHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index/postfile.html')
    def post(self, *args, **kwargs):
        self.set_secure_cookie("count", "100")
        u = self.get_body_argument("username")
        p = self.get_body_argument("passwd")
        self.render('index/showinfo.html', username=u, password=p)

class SetXsrfCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.xsrf_token
        self.write("ok")

class AjaxTestHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index/ajax.html')
    def post(self, *args, **kwargs):
        u = self.get_body_argument("username")
        p = self.get_body_argument("passwd")
        print("name = ", u)
        print("pass = ", p)
        # print(self.request.body)
        self.write("ok")