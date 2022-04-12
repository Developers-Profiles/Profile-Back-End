from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class TypeUser(models.TextChoices):
    BACK_END = 'Back End'
    FRONT_END = 'Front End'
    FULL_STACK = 'Full Stack'


class SocialNetworks(models.Model):
    name = models.CharField(max_length=50)
    link_sn = models.CharField(max_length=200)


class StatusUserModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True, null=True)
    social_networks = models.ForeignKey(SocialNetworks, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='img')
    type_user = models.CharField(max_length=11, choices=TypeUser.choices, default=TypeUser.FULL_STACK)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Type {self.type_user} by {self.user.id}"

    class Meta:
        verbose_name = 'StatusUserModel'
        verbose_name_plural = 'StatusUserModels'
        ordering = ['id']