from django.db import models
from django.contrib.auth.models import User

class SignImg(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images')

    def __str__(self):
        return self.user.username
