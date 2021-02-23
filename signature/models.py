from django.db import models
from django.contrib.auth.models import User

import os
def create_path(instance, filename):
    return os.path.join(
        instance.user.username,
        filename
    )

class SignImg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img1 = models.ImageField(upload_to=create_path, blank=True)
    img2 = models.ImageField(upload_to=create_path, blank=True)


    def __str__(self):
        return self.user.username
