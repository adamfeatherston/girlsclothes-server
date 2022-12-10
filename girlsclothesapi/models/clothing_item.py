from django.db import models

class ClothingItem(models.Model):

    item_description = models.CharField(max_length=50)
    clothing_type = models.ForeignKey('ClothingType', on_delete=models.CASCADE)
    kid = models.ForeignKey('Kid', on_delete=models.CASCADE)
    size = models.CharField(max_length=15)
    clean_or_dirty = models.BooleanField(null=True, blank=True)
    item_fits = models.BooleanField(null=True, blank=True)
    sibling_has_match = models.BooleanField()
    item_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, null=True, blank=True)
    clothing_uses = models.ManyToManyField("ClothingUse", through="ItemUse", related_name="clothing_uses")