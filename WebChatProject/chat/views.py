from django.shortcuts import render, redirect

from .models import Room
from .forms import RoomNameForm


def index(request):
    """Room name entering and go to chat with the room_name"""

    form = RoomNameForm(request.POST or None)

    # When the user entered a room name and submits it
    if request.method == 'POST':
        if form.is_valid():
            # get rom_name from form
            room_name = form.cleaned_data['room_name']
            # get a room with room_name from DB or create it in DB (if not exist)
            room, created = Room.objects.get_or_create(name=room_name)
            context = {"room_name": room_name}
            return render(request, "chat/chat.html", context)
        else:
            print(form.errors)

    return render(request, 'chat/index.html', context={'form': form})


def room(request, room_name):
    """If user is authenticated he gets chatPage.
    If user isn't authenticated he gets LoginView"""

    if not request.user.is_authenticated:
        return redirect("login_user")

    context = {"room_name": room_name}
    return render(request, "chat/chat.html", context)
