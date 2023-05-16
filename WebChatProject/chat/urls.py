from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordChangeView
from . import views

urlpatterns = [
    # chat
    path("", views.index, name="index"),
    path("chat/<str:room_name>/", views.room, name="room"),

    # login, logout
    # http://127.0.0.1:8000/auth/login/
    path("auth/login/", LoginView.as_view(template_name="chat/loginPage.html"), name="login_user"),
    path("auth/logout/", LogoutView.as_view(), name="logout_user"),

    # change password
    # http://127.0.0.1:8000/auth/change_password/
    path('auth/change_password/', PasswordChangeView.as_view(template_name='chat/change_password.html',
                                                             success_url='/'), name='change_password'),
]
