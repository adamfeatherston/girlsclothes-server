from django.db import models

class OutfitItem(models.Model):

    outfit = models.ForeignKey('Outfit', on_delete=models.CASCADE)
    clothing_item = models.ForeignKey('ClothingItem', on_delete=models.CASCADE)