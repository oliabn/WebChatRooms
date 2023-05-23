from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class UserRegisterForm(UserCreationForm):
    """User registration form."""

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RoomNameForm(forms.Form):
    """Form for room name entering."""

    room_name = forms.CharField(label="Room name",
                                required=True,
                                error_messages={'required': 'Please enter room name'})


class UserUpdateForm(forms.ModelForm):
    """UserUpdateForm to update a username and email."""

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """ProfileUpdateForm to update image."""
    class Meta:
        model = Profile
        fields = ['image']
