from django.db import models
from django.contrib.auth.models import AbstractUser
from user.manager import UserManager


class User(AbstractUser):
    username = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    email_verification_token = models.CharField(max_length=20, null=True, blank=True)
    forget_password_token = models.CharField(max_length=200, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = UserManager()

    def name(self):
        return self.first_name + ' '+ self.last_name

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id']
