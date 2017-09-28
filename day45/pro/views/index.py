import tornado.web
from tornado.web import RequestHandler

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index/index.html')

class SunckHandler(RequestHandler):
    def get(self, *args, **kwargs):
        per = {
            "name": "kaige",
            "temp": 18
        }
        self.render('index/sunck.html', **per)

class KaigeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pers = [
            {
                "name": "tom",
                "age": 18,
            },
            {
                "name": "jerry",
                "age": 16,
            },
            {
                "name": "sz",
                "age": 12,
            }
        ]
        self.render('index/kaige.html', flag=False, pers=pers)

class KaishenHandler(RequestHandler):
    def get(self, *args, **kwargs):
        def myS(x, y):
            return x + y
        self.render('index/kaishen.html', mySum=myS, num1=10, num2=20)

class KaikaiHandler(RequestHandler):
    def get(self, *args, **kwargs):
        str = "<h2>sunck is a good man</h2>"
        self.render('index/kaikai.html', str=str)

class KaihuangHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index/kaihuang.html', title='kaihuang')

class StudentsHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.application.db.insert("insert into students values('mm',12)")
        stuList = self.application.db.get_all_obj("select name,age from students", "students", "name", "age")
        print(stuList)
        self.render('index/students.html', stus=stuList)
        # self.write("ok")

# 普通cookie
class CommoncookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # self.set_cookie("sunck", "good")
        # self.set_header("Set-Cookie", "kaige=nice;Path=/")

        # 获取cookie
        cookie = self.get_cookie("sunck")
        print(cookie)

        # 清除cookie
        # self.clear_cookie(name, path="/", domain=None)
        self.clear_all_cookies()
        self.write("ok")

class SafecookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # self.set_secure_cookie("kaishen", "very nice")
        cookie = self.get_secure_cookie("kaishen")
        print(cookie)
        self.write("ok")

