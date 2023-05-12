Channels documentation: https://channels.readthedocs.io/en/stable/index.html  

Channels tutorial: https://channels.readthedocs.io/en/latest/tutorial/index.html

## How to install channels
1) Install channels (channels==3.0.4 for Django==4) to venv:  

    `python -m pip install -U channels`  

The installation process will be slightly different to use the channels==4.  

2) Add channels to installed apps in settings.py:

```python
INSTALLED_APPS = [
    'chat.apps.ChatConfig',

    'django.contrib.admin',
            ...
    'django.contrib.staticfiles',
     
    # add django channels
    'channels' ,
]
```

3) Set the ASGI application to y default ASGI file in the projectin in settings.py:  

    `ASGI_APPLICATION = 'WebChatProject.asgi.application'`  

### What also need to be added to setting.py:  

```python
ASGI_APPLICATION = 'WebChatProject.asgi.application'

"""Define the channel layer in which we will be working 
and sharing data """
# For Windows
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

# For Linux
# "default": {
#         "BACKEND": "asgi_redis.RedisChannelLayer",
#         "CONFIG": {
#             "hosts": [(redis_host, 6379)],
#         },
#     },
# }


# redirect url for login, logout
LOGIN_REDIRECT_URL = "index"

LOGOUT_REDIRECT_URL = "login-user"
```

## Redis

I run Redis by Docker.

* To start a Redis server on port 6379, run the following command:

`docker run -p 6379:6379 -d redis:5`  

* To make sure that the channel layer can communicate with Redis.  

Open a Django shell and run the following commands:  

```commandline
$ python manage.py shell
>>> import channels.layers
>>> channel_layer = channels.layers.get_channel_layer()
>>> from asgiref.sync import async_to_sync
>>> async_to_sync(channel_layer.send)('test_channel', {'type': 'hello'})
>>> async_to_sync(channel_layer.receive)('test_channel')
{'type': 'hello'}
```  

Type Control-D to exit the Django shell.

## How to test this chat
1) Install the required packages. 
* Django==4.2.1
* channels==3.0.4
* asgi-redis==1.4.3
* channels-redis==4.1.0  

2) Make migrations. In the terminal:

`cd WebChatProject`  

`python manage.py makemigrations`

`python manage.py migrate`  

3) You need to create 2 superusers through the terminal:  

`python manage.py createsuperuser`  

4) Run the server:  

`python manage.py runserver`  

5) Move to the site and start two different browsers. 
Login like two different users from different browsers.
6) Write messages in the chat