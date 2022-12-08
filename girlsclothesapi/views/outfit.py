from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from girlsclothesapi.models import Outfit, ClothingItem


class OutfitView(ViewSet):

    def list(self, request):

        outfit = Outfit.objects.all()
        serializer = OutfitSerializer(outfit, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):

        outfit = Outfit.objects.get(pk=pk)
        serializer = OutfitSerializer(outfit)
        return Response(serializer.data)

    def update(self, request, pk):

        outfit = Outfit.objects.get(pk=pk)
        outfit.outfit_description=request.data["outfit_description"]
        outfit.item_image=request.data["item_image"]

        outfit_dress = ClothingItem.objects.get(pk=request.data["clothing_item"])
        outfit_shirt = ClothingItem.objects.get(pk=request.data["clothing_item"])
        outfit_pant = ClothingItem.objects.get(pk=request.data["clothing_item"])
        outfit_shoe = ClothingItem.objects.get(pk=request.data["clothing_item"])
        outfit_sock = ClothingItem.objects.get(pk=request.data["clothing_item"])
        outfit_bow = ClothingItem.objects.get(pk=request.data["clothing_item"])

        outfit.dress.item = outfit_dress
        outfit.shirt.item = outfit_shirt
        outfit.pant_item = outfit_pant
        outfit.shoe_item = outfit_shoe
        outfit.sock_item = outfit_sock
        outfit.bow_item = outfit_bow
        outfit.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

class OutfitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Outfit
        fields = ('id', 'outfit_description', 'dress_item', 'shirt_item', 'pant_item', 'shoe_item', 'sock_item', 'bow_item', 'outfit_image')
