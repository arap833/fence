from django.db import models
from django.contrib.auth.models import  User
from PIL import Image

class Profile (models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    #fields to include
    image = models.ImageField(default='default.JPG',upload_to='profile_pics')
    fence_id = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)