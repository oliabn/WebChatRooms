from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse


class Room(models.Model):
    """Room names table"""

    name = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('room', args=[str(self.name)])


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


class Profile(models.Model):
    """User profile table"""

    # on_delete=models.CASCADE - delete profile when user is deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    rooms = models.ManyToManyField(Room)

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        """Override the save method of the model"""

        super().save(*args, **kwargs)

        # Open image
        img = Image.open(self.image.path)
        # resize image
        img = self.resize_image(img, 300)
        img.save(self.image.path)

        # resize image
        # if img.height > 300 or img.width > 300:
        #     output_size = (300, 300)
        #     # Resize image
        #     img.thumbnail(output_size)
        #     # Save it again and override the larger image
        #     img.save(self.image.path)

    @staticmethod
    def resize_image(image: Image, length: int) -> Image:
        """
        Resize an image to a square length x length. Return the resized image. It also crops
        part of the image; length: Width and height of the output image.
         Resizing strategy :
         1) resize the smallest side to the desired dimension (e.g. 300)
         2) crop the other side so as to make it fit with the same length as the smallest side (e.g. 300)
        """

        # If the height is bigger than width.
        if image.size[0] < image.size[1]:

            # this makes the width fit the LENGTH in pixels while conserving the ration.
            resized_image = image.resize((length, int(image.size[1] * (length / image.size[0]))))
            # amount of pixels to lose in total on the height of the image.
            required_loss = (resized_image.size[1] - length)
            # crop the height of the image so as to keep 300 pixels the center part.
            resized_image = resized_image.crop(
                box=(0, required_loss / 2, length, resized_image.size[1] - required_loss / 2))
            # we now have a length*length pixels image.

            return resized_image

        # If the width is bigger than the height.
        else:

            # this makes the height fit the LENGTH in pixels while conserving the ration.
            resized_image = image.resize((int(image.size[0] * (length / image.size[1])), length))
            # amount of pixels to lose in total on the width of the image.
            required_loss = resized_image.size[0] - length
            # crop the width of the image so as to keep 300 pixels of the center part.
            resized_image = resized_image.crop(
                box=(required_loss / 2, 0, resized_image.size[0] - required_loss / 2, length))
            # we now have a length*length pixels image.

            return resized_image
