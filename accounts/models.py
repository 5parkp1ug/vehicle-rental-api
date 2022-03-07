from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    model to store users
    """
    class Roles(models.TextChoices):
        ADMIN = 'A', 'Admin'
        CUSTOMER = 'C', 'Customer'

    role = models.CharField(max_length=1, choices=Roles.choices, default=Roles.CUSTOMER)

    def __str__(self):
        return self.username
