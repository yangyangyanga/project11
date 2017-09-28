import tornado.web

import config
from views import index
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', index.IndexHandler),
            (r'/yang', index.YangHandler, {"word1": "yang", "word2": "aaa"}),
            tornado.web.url(r'/kaige', index.KaigeHandler, {"a": "aaa", "b": "bbb"}, name="kk"),

            # 获取url的特定部分
            (r'/linzhiling/(\w+)/(\w+)', index.LinzhilingHandler),

            # 获取get请求的传参
            (r'/fan', index.FanHandler),
            (r'/fan1', index.FanHandler1),

            # 获取post请求的传参
            (r'/postfile', index.PostFileHandeler),
            (r'/submit', index.SubmitHandler),

            # request对象
            (r'/reqing', index.ReHandler),

            # 上传文件
            (r'/upfile', index.UpHandler),
            (r'/savefile', index.SaveFileHandler),

            # 利用write()方法返回json数据
            (r'/returnj', index.ReturnHandler),

            # 返回状态码
            (r'/restatus', index.RestatusHandler),

            # 重定向
            (r'/S', index.SHandler),
            (r'/s', index.sHandler),

            # 错误码
            (r'/mistake', index.MistakeHandler),

            # 接口调用顺序
            (r'/seque', index.SequeHandler),

        ]
        super(Application, self).__init__(handlers, **config.settings)