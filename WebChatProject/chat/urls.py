from django.urls import path, include
# from chat import  as chat_views
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # chat
    path("", views.index, name="index"),
    path("chat/<str:room_name>/", views.room, name="room"),

    # login, logout
    # http://127.0.0.1:8000/auth/login
    path("auth/login/", LoginView.as_view(template_name="chat/loginPage.html"), name="login_user"),
    path("auth/logout/", LogoutView.as_view(), name="logout_user"),
]
