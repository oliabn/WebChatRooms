from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Room
from .forms import RoomNameForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm


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


def register(request):
    """User registration"""

    # When the user filled out the form and submits it
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # save user to DB
            form.save()
            # get the username that is submitted from form
            username = form.cleaned_data.get('username')
            # redirect user to Index
            return redirect('login_user')
    else:
        form = UserRegisterForm()
    return render(request, 'chat/register.html', {'form': form})


@login_required
# Require user logged in before they can access profile page
def profile(request):
    """User profile"""

    # When the user filled out the form and submits it
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,
                                   instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            # save it in DB
            user_form.save()
            profile_form.save()
            # redirect back to profile page
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'user_form': user_form, 'profile_form': profile_form}

    return render(request, 'chat/profile.html', context)
