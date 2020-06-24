


# "id": "W012A3CDE",
# "real_name": "Egon Spengler",
# "tz": "America/Los_Angeles",

# import random 
from random import choice
import string 
import secrets
from uuid import uuid4

# dajngo imports
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

#external import 
from timezone_field import TimeZoneField
# from timezone_utils.choices import PRETTY_ALL_TIMEZONES_CHOICES

#app
from .managers import UserManager


def custom_id():
    alphabet = string.ascii_letters + string.digits
    generate_id = ''.join(secrets.choice(alphabet) for i in range(8))

    return generate_id

class User(AbstractBaseUser, PermissionsMixin):
    """
        Custom user model to generate user id,real_name and timezone,email is working here 
        as a main username field and email must be set
    """
    id = models.CharField(max_length = 9,primary_key=True, default=custom_id, editable=False)
    email = models.EmailField(unique=True)
    real_name = models.CharField(max_length = 100) 
    tz = TimeZoneField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class ActivityPeriod(models.Model):
    profile = models.ForeignKey(User,on_delete = models.CASCADE,
                                related_name = 'user_activity')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()




