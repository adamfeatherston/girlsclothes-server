from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from girlsclothesapi.models import Kid


class KidView(ViewSet):

    def list(self, request):

        kid = Kid.objects.all()
        serializer = KidSerializer(kid, many=True)
        return Response(serializer.data)

class KidSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kid
        fields = ('id', 'user', 'age', 'dress_size', 'shoe_size', 'shirt_size', 'pant_size', 'underwear_or_diaper_size', 'sock_size')