from django.db import models

class Outfit(models.Model):

    outfit_description = models.CharField(max_length=50)
    dress_item = models.ForeignKey('ClothingItem', on_delete=models.CASCADE, related_name='outfit_dress', null=True, blank=True)
    shirt_item = models.ForeignKey('ClothingItem', on_delete=models.CASCADE, related_name='outfit_shirt', null=True, blank=True)
    pant_item = models.ForeignKey('ClothingItem', on_delete=models.CASCADE, related_name='outfit_pant', null=True, blank=True)
    shoe_item = models.ForeignKey('ClothingItem', on_delete=models.CASCADE, related_name='outfit_shoe', null=True, blank=True)
    sock_item = models.ForeignKey('ClothingItem', on_delete=models.CASCADE, related_name='outfit_sock', null=True, blank=True)
    bow_item = models.ForeignKey('ClothingItem', on_delete=models.CASCADE, related_name='outfit_bow', null=True, blank=True)
    outfit_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, null=True, blank=True)
    