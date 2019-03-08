import environ

from .base import *


env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, 'settings/envs/.env'))

DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

DATABASES = {
    'default': env.db(),
    'extra': env.db('SQLITE_URL', default='sqlite:////tmp/my-tmp-sqlite.db'),
}
