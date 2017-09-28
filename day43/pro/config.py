import os
BASE_PATH = os.path.dirname(__file__)

options = {
    "port": 8080,
    "list": ["good", "handsome", "nice"],
}

# app的配置
settings = {
    'template_path': os.path.join(BASE_PATH, "templates"),
    'static_path': os.path.join(BASE_PATH, "static"),
    'debug': True,
}