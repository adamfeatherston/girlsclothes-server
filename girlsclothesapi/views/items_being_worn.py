from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from girlsclothesapi.models import ItemsBeingWorn, Outfit, ClothingItem


class ItemsBeingWornView(ViewSet):

    def list(self, request):

        worn = ItemsBeingWorn.objects.all()
        serializer = ItemsBeingWornSerializer(worn, many=True)
        return Response(serializer.data)

    def create(self, request):

        outfit = Outfit.objects.get(pk=request.data["outfitId"])
        clothing_item = ClothingItem.objects.get(pk=request.data["clothingItemId"])

        wearing = ItemsBeingWorn.objects.create(
            outfit=outfit,
            clothing_item=clothing_item
        )
        serializer = ItemsBeingWornSerializer(wearing)
        return Response(serializer.data)

class ItemsBeingWornSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemsBeingWorn
        fields = ('id', 'outfit', 'clothing_item')