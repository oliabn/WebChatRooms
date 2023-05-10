from django.urls import path, include
# from chat import  as chat_views
from .views import chatPage
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # chat
    path("", chatPage, name="chat-page"),

    # login
    # http://127.0.0.1:8000/auth/login
    path("auth/login/", LoginView.as_view(template_name="chat/loginPage.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
]
