from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class Profile(models.Model):
    """User profile table"""

    # on_delete=models.CASCADE - delete profile when user is deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'


class Room(models.Model):
    """Room names table"""

    name = models.TextField()

    def __str__(self):
        return self.name


class Message(models.Model):
    """To store messages"""

    room = models.ForeignKey(Room,
                             related_name='messages',
                             null=True,
                             on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(),
                             null=True,
                             blank=True,
                             on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'room: {self.room.name}, user: {self.user.username}, time: {self.timestamp}'
