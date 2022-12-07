from django.db import models

class ClothingUse(models.Model):

    use = models.CharField(max_length=10)