import uuid

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="user")
    phone_number = models.CharField(max_length=100)
    otp = models.CharField(max_length=100)
    uid = models.UUIDField(default=uuid.uuid4)



