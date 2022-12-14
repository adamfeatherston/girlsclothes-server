from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from girlsclothesapi.models import ClothingItem, Kid, ClothingType, ClothingUse, ItemUse


class ClothingItemView(ViewSet):

    def list(self, request):

        if request.auth.user.is_staff:
            items = ClothingItem.objects.all().order_by('clothing_type')

            for item in items:
                item.creator=False
                if item.kid.user==request.auth.user:
                    item.creator=True

            if "type" in request.query_params:
                items = items.filter(clothing_type_id=request.query_params['type'])
                if request.query_params['type'] == "{id}":
                    pass

            elif "isClean" in request.query_params:
                items = items.filter(clean_or_dirty=True)
                if request.query_params['isClean'] == True:
                    pass

            elif "siblingMatch" in request.query_params:
                items = items.filter(sibling_has_match=True)
                if request.query_params['siblingMatch'] == True:
                    pass

            elif "kid" in request.query_params:
                items = items.filter(kid_id=request.query_params['kid'])
                if request.query_params['kid'] == "{id}":
                    pass

        else:
            items = ClothingItem.objects.filter(kid__user=request.auth.user).order_by('clothing_type')

            if "type" in request.query_params:
                items = items.filter(clothing_type_id=request.query_params['type'])
                if request.query_params['type'] == "{id}":
                    pass

            elif "isClean" in request.query_params:
                items = items.filter(clean_or_dirty=True)
                if request.query_params['isClean'] == True:
                    pass

            elif "siblingMatch" in request.query_params:
                items = items.filter(sibling_has_match=True)
                if request.query_params['siblingMatch'] == True:
                    pass

        
        serializer = ClothingItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):

        if request.auth.user.is_staff:
            item = ClothingItem.objects.get(pk=pk)

        else:
            item = ClothingItem.objects.filter(kid__user=request.auth.user)

        serializer = ClothingItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):

        if request.auth.user.is_staff:

            required_fields = ['item_description', 'clothing_type', 'kid', 'size', 'clean_or_dirty', 'item_fits', 'sibling_has_match', 'item_image', 'clothing_uses']
            missing_fields = "Please send all required fields"
            is_field_missing = False

            for field in required_fields:
                value = request.data.get(field, None)
                if value is None:
                    missing_fields = f'{missing_fields} and {field}'
                    is_field_missing = True
            
            if is_field_missing:
                return Response({"message": missing_fields}, status = status.HTTP_400_BAD_REQUEST)

            uses = request.data["clothing_uses"]
            for use in uses:
                try:
                    use_to_assign = ClothingUse.objects.get(pk=use)
                except ClothingUse.DoesNotExist:
                    return Response({"message": "The use you specified does not exist"}, status = status.HTTP_404_NOT_FOUND)

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

            for use in uses:
                use_to_assign = ClothingUse.objects.get(pk=use)
                item_use = ItemUse()
                item_use.clothing_item = item
                item_use.clothing_use = use_to_assign
                item_use.save()


            serializer = ClothingItemSerializer(item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):

        if request.auth.user.is_staff:
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
            item.clothing_uses.set(request.data["clothing_uses"])
            item.save()

        else:
            item = ClothingItem.objects.filter(kid__user=request.auth.user)
            item.item_description=request.data["item_description"]
            item.size=request.data["size"]
            item.clean_or_dirty=request.data["clean_or_dirty"]
            item.item_fits=request.data["item_fits"]
            item.sibling_has_match=request.data["sibling_has_match"]
            item.item_image=request.data["item_image"]

            clothing_type = ClothingType.objects.get(pk=request.data["clothing_type"])
            kid = Kid.objects.filter(kid__user=request.auth.user)
            item.clothing_type = clothing_type
            item.kid=kid
            item.clothing_uses.set(request.data["clothing_uses"])
            item.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        
        if request.auth.user.is_staff:
            item = ClothingItem.objects.get(pk=pk)
            item.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True)
    def adduses(self, request, pk):

        if request.auth.user.is_staff:
            use = ClothingUse.objects.get(pk=request.data['clothing_uses'])
            outfit = ClothingItem.objects.get(pk=pk)
            outfit.clothing_uses.add(use)
        return Response({'message': 'Clothing use added to this item'}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=True)
    def removeuses(self, request, pk):

        if request.auth.user.is_staff:
            use = ClothingUse.objects.get(pk=request.data['clothing_uses'])
            outfit = ClothingItem.objects.get(pk=pk)
            outfit.clothing_uses.remove(use)
        return Response({'message': 'Clothing use removed from this item'}, status=status.HTTP_204_NO_CONTENT)

class ClothingUseSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClothingUse
        fields = ('use')

class ClothingTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClothingType
        fields = ('type')

class ClothingKidSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kid
        fields = ('nickname')

class ClothingItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClothingItem
        fields = ('id', 'item_description', 'clothing_type', 'item_type', 'kid', 'kid_nickname', 'size', 'clean_or_dirty', 'item_fits', 'sibling_has_match', 'item_image', 'clothing_uses', 'item_uses', 'creator')
        depth = 1
        