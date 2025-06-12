from .settings import *
import os

# Keep DEBUG True for now to see errors
DEBUG = True

# Render domain
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.onrender.com',
]

# Use environment DATABASE_URL if available, otherwise fall back to default
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ['DATABASE_URL'])
    }