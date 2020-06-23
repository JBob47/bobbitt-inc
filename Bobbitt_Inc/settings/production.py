from ._base import *

import json

with open('/etc/config.json') as config_file:
    config = json.load(config_file)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['www.bobbitt-inc.com', '172.105.159.189']