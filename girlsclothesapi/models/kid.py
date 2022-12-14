from django.db import models
from django.contrib.auth.models import User


class Kid(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=15, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    dress_size = models.CharField(max_length=5, null=True, blank=True)
    shoe_size = models.CharField(max_length=5, null=True, blank=True)
    shirt_size = models.CharField(max_length=5, null=True, blank=True)
    pant_size = models.CharField(max_length=5, null=True, blank=True)
    underwear_or_diaper_size = models.CharField(max_length=5, null=True, blank=True)
    sock_size = models.CharField(max_length=5, null=True, blank=True)

