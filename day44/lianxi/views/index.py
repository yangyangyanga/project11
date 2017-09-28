from tornado.web import RequestHandler

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        url = self.reverse_url("kk")
        print(url)
        # self.write("hello ~")
        self.write("<a href='%s'>play</a>"%(url))

class YangHandler(RequestHandler):
    def initialize(self, word1, word2):
        self.a = word1
        self.b = word2
    def get(self, *args, **kwargs):
        self.write(self.a + "--" + self.b)

class KaigeHandler(RequestHandler):
    def initialize(self, a, b):
        self.w1 = a
        self.w2 = b
    def get(self, *args, **kwargs):
        self.write(self.w1 + "==" + self.w2)

class LinzhilingHandler(RequestHandler):
    def get(self, a1, a2, *args, **kwargs):
        self.write(a1 + "--" + a2)

class FanHandler(RequestHandler):
    def get(self, *args, **kwargs):
        a = self.get_query_argument("a")
        b = self.get_query_argument("b")
        self.write(a + "-" + b)
class FanHandler1(RequestHandler):
    def get(self, *args, **kwargs):
        a = self.get_query_arguments("a")
        b = self.get_query_argument("c")
        print(type(a))
        self.write(a[0] + "--" + a[1] + "--" + b)

class PostFileHandeler(RequestHandler):
    def get(self, *args, **kwargs):
        a = self.get_argument("a")
        print(a)
        bl = self.get_arguments("b")
        print(bl)
        self.render("index/postfile.html")
class SubmitHandler(RequestHandler):
    def post(self, *args, **kwargs):
        username = self.get_body_argument("username")
        passwd = self.get_body_argument("passwd")
        hobby = self.get_body_arguments("hobby")
        user = self.get_argument("username")
        print(user)
        print(username)
        print(passwd)
        print(hobby)
        self.write("成功提交" + user)

class ReHandler(RequestHandler):
    def get(self, *args, **kwargs):
        print(self.request.method)
        print(self.request.host)
        print(self.request.uri)
        print(self.request.path)
        print(self.request.query)
        print(self.request.version)
        print(self.request.headers)
        print(self.request.body)
        print(self.request.remote_ip)
        print(self.request.files)

    def post(self, *args, **kwargs):
        print(self.request.method)

import config
class UpHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index/upfilem.html")
class SaveFileHandler(RequestHandler):
    def post(self, *args, **kwargs):
        files = self.request.files
        print(files)
        for fii in files:
            print("fii = ", fii)
            file = files[fii]
            print(file)
            for filen in file:
                print(filen)
                filePath = config.BASE_PATH + "/upfile/" + filen["filename"]
                with open(filePath, "wb") as f:
                    f.write(filen["body"])
        self.write("ok")

import json
class ReturnHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", "application/json; charset=utf-8")
        self.set_header("yang", "hello")
    def get(self, *args, **kwargs):
        per = {
            "name": "yang",
            "age": 18,
            "hooby": "sing",
        }
        j = json.dumps(per)
        # self.set_header("Content-Type", "application/json; charset=utf-8")
        self.set_header("yang", "haha")
        self.write(j)

        # self.write(per)

class RestatusHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("sunck is a good man")
        self.set_status(999, "what")

class SHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.redirect("/s")
class sHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('我是重定向的界面')

class MistakeHandler(RequestHandler):
    def write_error(self, status_code, **kwargs):
        if status_code == 500:
            self.write("<h1>服务器内部错误</h1>")
        elif status_code == 200:
            self.write("<h1>haha</h1>")

    def get(self, *args, **kwargs):
        self.write("zz")
        # self.send_error(500)
        self.send_error(200)

class SequeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        print("我是get方法")
        self.send_error(200)
    def initialize(self):
        print("我是initialize")
    def set_default_headers(self):
        print("我是set_default_headers")
    def write_error(self, status_code, **kwargs):
        print("我是write_error")
    def prepare(self):
        print("我是prepare")
    def on_finish(self):
        print("我是on_finish")
