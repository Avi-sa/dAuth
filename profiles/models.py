from django.db import models
# from django.contrib.auth import User
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validate_number(number):
    if len(number) < 10:
        raise ValidationError("Enter a valid phone number")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=14, unique=True, null=True, blank=True, validators=[validate_number])
    is_manager = models.BooleanField(default=None, null=True)

    class Meta:
        permissions = (("can_evaluate_all", "Evaluate all the employees"),)

    def __str__(self):
        return self.user.username