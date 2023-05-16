from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
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
    path('auth/change_password/', PasswordChangeView.as_view(
        template_name='chat/change_password.html',
        success_url='/'),
         name='change_password'),

    # forget password
    # http://127.0.0.1:8000/auth/password_reset/
    # Password Reset
    path('auth/password_reset/', PasswordResetView.as_view(
        template_name='chat/password_reset/password_reset.html'), name='password_reset'),
    # Password Reset Done
    path('auth/password_reset/done/', PasswordResetDoneView.as_view(
        template_name='chat/password_reset/password_reset_done.html'),
         name='password_reset_done'),
    # Password Reset Confirm
    path('auth/password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='chat/password_reset/password_reset_confirm.html'),
         name='password_reset_confirm'),
    # Password Reset Complete
    path('auth/password_reset_complete/', PasswordResetCompleteView.as_view(
        template_name='chat/password_reset/password_reset_complete.html'),
         name='password_reset_complete'),
]
