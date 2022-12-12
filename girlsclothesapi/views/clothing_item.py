from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from girlsclothesapi.models import ClothingItem, Kid, ClothingType, ClothingUse


class ClothingItemView(ViewSet):

    def list(self, request):

        item = ClothingItem.objects.all()
        serializer = ClothingItemSerializer(item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):

        item = ClothingItem.objects.get(pk=pk)
        serializer = ClothingItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):

        clothing_type= ClothingType.objects.get(pk=request.data["clothing_type"])
        kid = Kid.objects.get(pk=request.data["kid"])

        item = ClothingItem.objects.create(
            item_description=request.data["item_description"],
            size=request.data["size"],
            clean_or_dirty=request.data["clean_or_dirty"],
            item_fits=request.data["item_fits"],
            sibling_has_match=request.data["sibling_has_match"],
            item_image=request.data["item_image"],
            clothing_type=clothing_type,
            kid=kid
        )

        serializer = ClothingItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):

        item = ClothingItem.objects.get(pk=pk)
        item.item_description=request.data["item_description"]
        item.size=request.data["size"]
        item.clean_or_dirty=request.data["clean_or_dirty"]
        item.item_fits=request.data["item_fits"]
        item.sibling_has_match=request.data["sibling_has_match"]
        item.item_image=request.data["item_image"]

        clothing_type = ClothingType.objects.get(pk=request.data["clothing_type"])
        kid = Kid.objects.get(pk=request.data["kid"])
        item.clothing_type = clothing_type
        item.kid=kid
        item.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        item = ClothingItem.objects.get(pk=pk)
        item.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True)
    def adduses(self, request, pk):

        use = ClothingUse.objects.get(pk=request.data['clothing_uses'])
        outfit = ClothingItem.objects.get(pk=pk)
        outfit.clothing_uses.add(use)
        return Response({'message': 'Clothing use added to this outfit'}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=True)
    def removeuses(self, request, pk):

        use = ClothingUse.objects.get(pk=request.data['clothing_uses'])
        outfit = ClothingItem.objects.get(pk=pk)
        outfit.clothing_uses.remove(use)
        return Response({'message': 'Clothing use removed from this outfit'}, status=status.HTTP_204_NO_CONTENT)

class ClothingItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClothingItem
        fields = ('id', 'item_description', 'clothing_type', 'kid', 'size', 'clean_or_dirty', 'item_fits', 'sibling_has_match', 'item_image', 'clothing_uses')
        depth = 2
        