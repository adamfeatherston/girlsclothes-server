from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from girlsclothesapi.models import Outfit, ClothingItem, Kid


class OutfitView(ViewSet):

    def create(self, request):

        if request.auth.user.is_staff:
            outfit = Outfit.objects.create(
                outfit_description=request.data["outfit_description"],
                outfit_image=request.data["outfit_image"]
            )

        serializer = OutfitSerializer(outfit)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):

        
        outfit = Outfit.objects.all()

        if "kid" in request.query_params:
            outfit = outfit.filter(kid_id=request.query_params['kid'])
            if request.query_params['kid'] == "{id}":
                pass


        serializer = OutfitSerializer(outfit, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):

        if request.auth.user.is_staff:
            outfit = Outfit.objects.get(pk=pk)
        else:
            outfit = Outfit.objects.filter(kid__user=request.auth.user)

        serializer = OutfitSerializer(outfit)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk):

        if request.auth.user.is_staff:
            outfit = Outfit.objects.get(pk=pk)
            outfit.outfit_description=request.data["outfit_description"]
            outfit.outfit_image=request.data["outfit_image"]
            outfit.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        
        if request.auth.user.is_staff:
            item = Outfit.objects.get(pk=pk)
            item.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True)
    def additems(self, request, pk):

        if request.auth.user.is_staff:
            item = ClothingItem.objects.get(pk=request.data['clothing_items'])
            outfit = Outfit.objects.get(pk=pk)
            outfit.clothing_items.add(item)
        return Response({'message': 'Clothing item added to this outfit'}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=True)
    def removeitems(self, request, pk):

        if request.auth.user.is_staff:
            item = ClothingItem.objects.get(pk=request.data['clothing_items'])
            outfit = Outfit.objects.get(pk=pk)
            outfit.clothing_items.remove(item)
        return Response({'message': 'Clothing item removed from this outfit'}, status=status.HTTP_204_NO_CONTENT)

class OutfitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Outfit
        fields = ('id', 'outfit_description', 'outfit_image', 'clothing_items')
        depth = 2

        