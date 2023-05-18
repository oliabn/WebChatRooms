from django.shortcuts import render, redirect

from .models import Room


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    """If user is authenticated he gets chatPage.
    If user isn't authenticated he gets LoginView"""

    if not request.user.is_authenticated:
        return redirect("login_user")

    room, created = Room.objects.get_or_create(name=room_name)

    context = {"room_name": room_name}
    return render(request, "chat/chat.html", context)
