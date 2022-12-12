from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from girlsclothesapi.models import ClothingUse


class ClothingUseView(ViewSet):

    def list(self, request):

        use = ClothingUse.objects.all()
        serializer = ClothingUseSerializer(use, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ClothingUseSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClothingUse
        fields = ('id', 'use')