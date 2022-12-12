from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from girlsclothesapi.models import ClothingType


class ClothingTypeView(ViewSet):

    def list(self, request):

        type = ClothingType.objects.all()
        serializer = ClothingTypeSerializer(type, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ClothingTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClothingType
        fields = ('id', 'type')