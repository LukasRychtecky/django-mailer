DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        },
    }

INSTALLED_APPS = [
    'mailer',
    ]

SECRET_KEY = 'x'
