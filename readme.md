
* Reference : [Server World](https://www.server-world.info/en/note?os=Rocky_Linux_8&p=python&f=3)

## start project
```bash
## create project
django-admin startproject administrate

## create DB
cd administrate/
python manage.py migrate

## create root user
python manage.py createsuperuser
```
<br>
### `python manage.py createsuperuser`

```bash
[rocky@deneil-control-node administrate]$ python manage.py createsuperuser
Username (leave blank to use 'rocky'): rocky
Email address: hudeneil@gmail.com
Password: 
Password (again): 
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
[rocky@deneil-control-node administrate]$ 
```


## create new app

```bash
## create new app "test_app"
python manage.py startapp test_app


## create new
vi test_app/views.py

## redirt app root url to test_app/url.py 
vi administrate/urls.py

## setting app root url
vi test_app/urls.py

## change settings
vi administrate/settings.py
```

### `test_app/views.py`
```python
# add to the end
from django.http import HttpResponse
def main(request):
    html = '<html>\n' \
           '<body>\n' \
           '<div style="width: 100%; font-size: 40px; font-weight: bold; text-align: center;">\n' \
           'Django Test Page\n' \
           '</div>\n' \
           '</body>\n' \
           '</html>\n'
    return HttpResponse(html)

```

### `administrate/urls.py`
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_app/', include('test_app.urls')),
]

```

### `test_app/urls.py`
```bash
from django.urls import path
from .views import main

urlpatterns = [
    path('', main, name='home')
]
```

### `administrate/settings.py`
```python

import os
from pathlib import Path

...
ALLOWED_HOSTS = ['*']

...

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'test_app',
]

...

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
...

LANGUAGE_CODE = 'zh-Hant'

TIME_ZONE = 'Asia/Taipei'
...

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

...
```
----

<br>

## create new app (secretManager)















