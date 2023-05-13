from django.db import models
from django.contrib.auth import get_user_model


class Message(models.Model):
    """To store messages"""

    user = models.ForeignKey(get_user_model(),
                             null=True,
                             blank=True,
                             on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
