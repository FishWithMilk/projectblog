from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from PIL import Image


class CustomUser(AbstractUser):
    image = models.ImageField(default='avatar_default.png', upload_to='profile_pics')

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    def __str__(self):
        return f'{self.username}'



# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     #username_profile = user.username
#     image = models.ImageField(default='avatar_default.png', upload_to='profile_pics')
#
#     def __str__(self):
#         return f'{self.user.username} Profile'
#
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         img = Image.open(self.image.path)
#         if img.height > 300 or img.width > 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size)
#             img.save(self.image.path)
