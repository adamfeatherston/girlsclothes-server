from django.db import models

class Outfit(models.Model):

    outfit_description = models.CharField(max_length=50)
    outfit_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, null=True, blank=True)
