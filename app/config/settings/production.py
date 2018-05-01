from .base import *

secrets = json.loads(open(SECRETS_PRODUCTION, 'rt').read())
DEBUG = False
ALLOWED_HOSTS = [
    '.amazonaws.com',
]
DATABASES = secrets['DATABASES']
