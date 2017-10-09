import os
BASE_PATH = os.path.dirname(__file__)

options = {
    "port": 9000,
}

settings = {
    'template_path': os.path.join(BASE_PATH, 'templates'),
    'static_path': os.path.join(BASE_PATH, 'static'),
    'debug': True,
    'cookie_secret': "QJtxviY2TiWyvHuKSEJH6/OzkGzFfEOkgrSXruDU6k4=",
    'xsrf_cookies': True,
}