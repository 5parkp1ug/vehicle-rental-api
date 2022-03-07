from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from rentalAPI import settings


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


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)