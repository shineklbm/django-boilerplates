DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# guys we are disabling cache for local development,
# please make sure to disable this for live sites
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# guys we are configuring this for local mail server setup,
# please make sure to disable this also on live
# to test mail on terminal please use the following command
# python -m smtpd -n -c DebuggingServer localhost:1025
# or you can see the mails as a file with the new settings I added EMAIL_FILE_PATH

if DEBUG:
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_USE_TLS = False
    DEFAULT_FROM_EMAIL = 'testing@example.com'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    EMAIL_FILE_PATH = os.path.join(os.path.dirname(BASE_DIR), 'emails')

# guys I have appended the debug_toolbar
# the following settings are there for debug toolbar
# you guys may use this for debugging purpose
INSTALLED_APPS += [
    'debug_toolbar',
]
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
INTERNAL_IPS = '127.0.0.1'
