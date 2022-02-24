"""
Defines the user model and other related structures.
"""
from typing import Any, Dict, List, Optional, Type

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from user.utils import send_activate_email

class UserManager(BaseUserManager):
    """
    This class extends the base UserManager to provide utilities for adding
    more users.
    """

    def create_user(
        self,
        email: str,
        name: str,
        username: str,
        password: Optional[str] = None
    ) -> "User":
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            username=username
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
        email: str,
        name: str,
        username: str,
        password: Optional[str] = None,
    ) -> "User":
        if password is None:
            raise TypeError("Password should not be none")

        user = self.create_user(email, name, username, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_verified = True
        user.is_active = True
        user.save()
        return user




class User(AbstractBaseUser):
    """
    This class extends the base User class to provide the fields needed for operating
    the SecurityPal app.
    """

    email = models.EmailField(max_length=255, unique=True, db_index=True)
    username = models.CharField(max_length=25,unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["name", "email"]

    objects = UserManager()

    def __str__(self) -> str:
        return str(self.email)

    def has_perm(
        self, perm: Any, obj: Any = None  # pylint: disable=unused-argument
    ) -> bool:
        return self.is_superuser

    def has_module_perms(
        self, app_label: Any  # pylint: disable=unused-argument
    ) -> bool:
        return self.is_superuser


@receiver(post_save, sender=User)
def send_activation_email(sender, instance, created, **kwargs):

    if created:
        send_activate_email(instance)