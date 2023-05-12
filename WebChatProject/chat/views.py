from django.shortcuts import render, redirect


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    """If user is authenticated he gets chatPage.
    If user isn't authenticated he gets LoginView"""

    if not request.user.is_authenticated:
        return redirect("login-user")

    context = {"room_name": room_name}
    return render(request, "chat/chatPage.html", context)
