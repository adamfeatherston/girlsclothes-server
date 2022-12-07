from django.db import models

class ItemUse(models.Model):

    clothing_item = models.ForeignKey('ClothingItem', on_delete=models.CASCADE)
    clothing_use = models.ForeignKey('ClothingUse', on_delete=models.CASCADE)