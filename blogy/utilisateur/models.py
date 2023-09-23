from django.db import models
from django.contrib.auth.models import User
import os
from .utils import image_resize


def renommer_image(instance, filename):
    upload_to = 'image/'
    ext = filename.split('.')[-1]
    if instance.user.username:
        filename = 'photo_profile/{}.{}'.format(instance.user.username, ext)
        return os.path.join(upload_to, filename)

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models
                                .CASCADE)
    bio = models.CharField(max_length=150, blank=True)
    photo_profile = models.ImageField(upload_to=renommer_image)
    admin = 'admin'
    utilisateur = 'user'

    type_user = [
        (admin, 'admin'), (utilisateur, 'user')
    ]
    type_profile = models.CharField(max_length=100, choices=type_user)

    def __str__(self):
        return self.user.username

    def save(self, commit=True, *args, **kwargs):

        if commit:
            image_resize(self.photo_profile, 105, 105)
            super().save(*args, **kwargs)
