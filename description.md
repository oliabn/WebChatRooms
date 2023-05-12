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
"""Define the channel layer in which we will be working 
and sharing data """
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

# redirect url for login, logout
LOGIN_REDIRECT_URL = "chat-page"

LOGOUT_REDIRECT_URL = "login-user"
```

## How to test this chat
1) Install the required packages. In the terminal  

`pip install -r requirements\requirements.txt`  

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