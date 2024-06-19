from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from pub.models import CreateUpdateModel
from django.db import models
from django.contrib.auth.models import BaseUserManager, UserManager


class UserProfileManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class UserProfile(AbstractBaseUser, CreateUpdateModel, PermissionsMixin):
    first_name = models.CharField(max_length=64, blank=False, null=False)
    last_name = models.CharField(max_length=64, blank=False, null=False)

    email = models.EmailField(unique=True, blank=False, null=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserProfileManager()
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email
