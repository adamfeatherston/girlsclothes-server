from django.db import models

class ClothingType(models.Model):

    type = models.CharField(max_length=10)
    