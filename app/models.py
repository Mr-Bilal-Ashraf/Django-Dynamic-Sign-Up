from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import Group, Permission
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models

import os


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Email address cannot be null/blank.")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=self.normalize_email(email), password=password)
        user.is_admin = True
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class TenantUser(AbstractUser):
    username = None
    first_name = models.CharField(
        _("first name"), max_length=255, null=True, blank=True
    )
    last_name = models.CharField(_("last name"), max_length=255, null=True, blank=True)
    email = models.EmailField(_("email address"), unique=True, db_index=True)

    user_permissions = models.ManyToManyField(Permission, blank=True)
    groups = models.ManyToManyField(Group, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(TenantUser, on_delete=models.CASCADE)
    data = models.JSONField()

    def __str__(self):
        return f"Profile Data of {self.user.email}"


def user_file_upload_to(instance, filename):
    user_dir = f"user_{instance.user.id}"
    return os.path.join("user_profile_data", user_dir, filename)


class Files(models.Model):
    user = models.ForeignKey(TenantUser, on_delete=models.CASCADE, related_name="files")
    file = models.FileField(upload_to=user_file_upload_to)
    name = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        if not self.name and self.file:
            self.name = self.file.name
        super().save(*args, **kwargs)
