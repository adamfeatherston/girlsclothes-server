from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from girlsclothesapi.models import ClothingItem


class ClothingItemView(ViewSet):

    def list(self, request):

        item = ClothingItem.objects.all()
        serializer = ClothingItemSerializer(item, many=True)
        return Response(serializer.data)

class ClothingItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClothingItem
        fields = ('id', 'item_description', 'clothing_type', 'kid', 'size', 'clean_or_dirty', 'item_fits', 'sibling_has_match', 'item_image')