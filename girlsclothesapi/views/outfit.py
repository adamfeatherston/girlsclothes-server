from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from girlsclothesapi.models import Outfit


class OutfitView(ViewSet):

    def list(self, request):

        outfit = Outfit.objects.all()
        serializer = OutfitSerializer(outfit, many=True)
        return Response(serializer.data)

class OutfitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Outfit
        fields = ('id', 'outfit_description', 'dress_item', 'shirt_item', 'pant_item', 'shoe_item', 'sock_item', 'bow_item', 'outfit_image')