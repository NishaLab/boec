from django import db
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from .enums import *


class User(AbstractUser):
    discriminator = models.CharField(db_column='Discriminator', max_length=255)  # Field name made lowercase.
    role = models.SmallIntegerField(
        null=False,
        blank=False,
        default=UserRole.CUSTOMER.value,
        choices=[
            (UserRole.CUSTOMER.value, UserRole.CUSTOMER.name),
            (UserRole.ADMIN.value, UserRole.ADMIN.name)
        ]
    )
    status = models.CharField(db_column='status', max_length=100, default="Available")