import os
# config.py文件所在的绝对路径
BASE_PATH = os.path.dirname(__file__)

options = {
    "port": 8880,
}

# app的配置
settings = {
    'template_path': os.path.join(BASE_PATH, "templates"),
    'static_path': os.path.join(BASE_PATH, "static"),
    'debug': True,
}
