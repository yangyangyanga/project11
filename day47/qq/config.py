import os
BASE_PATH = os.path.dirname(__file__)

options = {
    "port": 8000,
}

settings = {
    "template_path": os.path.join(BASE_PATH, 'templates'),
    "static_path": os.path.join(BASE_PATH, 'static'),
    "debug": True,
    'login_url': '/login',
}
