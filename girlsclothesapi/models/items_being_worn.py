from django.db import models

class ItemsBeingWorn(models.Model):

    outfit = models.ForeignKey('Outfit', on_delete=models.CASCADE)
    clothing_item = models.ForeignKey('ClothingItem', on_delete=models.CASCADE)