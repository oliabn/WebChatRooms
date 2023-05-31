from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from . import views

urlpatterns = [
    # chat
    path("", views.index, name="index"),
    path("chat/<str:room_name>/", views.room, name="room"),

    # user profile
    # http://127.0.0.1:8000/profile/
    path('profile/', views.profile, name='profile'),
    # delete room from user profile
    path('delete_room/', views.delete_room, name='delete_room'),

    # login, logout
    # http://127.0.0.1:8000/auth/login/
    path("accounts/login/", LoginView.as_view(template_name="chat/login.html"), name="login_user"),
    path("accounts/logout/", LogoutView.as_view(), name="logout_user"),

    # user registration
    # http://127.0.0.1:8000/auth/register/
    path("accounts/register/", views.register, name="register"),

    # change password
    # http://127.0.0.1:8000/auth/change_password/
    path('accounts/change_password/', PasswordChangeView.as_view(
        template_name='chat/change_password.html',
        success_url='/'),
         name='change_password'),

    # forget password
    # http://127.0.0.1:8000/auth/password_reset/
    # Password Reset
    path('accounts/password_reset/', PasswordResetView.as_view(
        template_name='chat/password_reset/password_reset.html'), name='password_reset'),
    # Password Reset Done
    path('accounts/password_reset/done/', PasswordResetDoneView.as_view(
        template_name='chat/password_reset/password_reset_done.html'),
         name='password_reset_done'),
    # Password Reset Confirm
    path('accounts/password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='chat/password_reset/password_reset_confirm.html'),
         name='password_reset_confirm'),
    # Password Reset Complete
    path('accounts/password_reset_complete/', PasswordResetCompleteView.as_view(
        template_name='chat/password_reset/password_reset_complete.html'),
         name='password_reset_complete'),
]
