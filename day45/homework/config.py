import os
# 获得当前文件的绝对路径
BASE_PATH = os.path.dirname(__file__)

options = {
    "port": 9000,
}

# app的配置
settings = {
    "template_path": os.path.join(BASE_PATH, "templates"),
    "static_path": os.path.join(BASE_PATH, "static"),
    "debug": True,
    "cookie_secret": "4imsl4qSSvySQWE1uyf4GkJr76tx1UErhPOEx2oXvJg=",
}