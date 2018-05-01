from .base import *

secrets = json.loads(open(SECRETS_DEV, 'rt').read())
DEBUG = True
ALLOWED_HOSTS = []
DATABASES = secrets['DATABASES']
