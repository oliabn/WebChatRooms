from django import forms


class RoomNameForm(forms.Form):
    """
    Form for room name entering
    """
    room_name = forms.CharField(label="Room name",
                                required=True,
                                error_messages={'required': 'Please enter room name'})
