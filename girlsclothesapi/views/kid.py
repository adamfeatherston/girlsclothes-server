from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from girlsclothesapi.models import Kid

class KidView(ViewSet):

    def list(self, request):

        if request.auth.user.is_staff:
            kid = Kid.objects.all()
            serializer = KidSerializer(kid, many=True)


        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):

        if request.auth.user.is_staff:
            kid = Kid.objects.get(pk=pk)
            serializer = KidSerializer(kid)
        else:
            kid = Kid.objects.filter(kid__user=request.auth.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk):

        if request.auth.user.is_staff:
            kid = Kid.objects.get(pk=pk)
            kid.nickname=request.data["nickname"]
            kid.age=request.data["age"]
            kid.dress_size=request.data["dress_size"]
            kid.shoe_size=request.data["shoe_size"]
            kid.shirt_size=request.data["shirt_size"]
            kid.pant_size=request.data["pant_size"]
            kid.underwear_or_diaper_size=request.data["underwear_or_diaper_size"]
            kid.sock_size=request.data["sock_size"]
            kid.save()

        else:
            kid = Kid.objects.filter(kid__user=request.auth.user)
            kid.nickname=request.data["nickname"]
            kid.age=request.data["age"]
            kid.dress_size=request.data["dress_size"]
            kid.shoe_size=request.data["shoe_size"]
            kid.shirt_size=request.data["shirt_size"]
            kid.pant_size=request.data["pant_size"]
            kid.underwear_or_diaper_size=request.data["underwear_or_diaper_size"]
            kid.sock_size=request.data["sock_size"]
            kid.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

class KidSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kid
        fields = ('id', 'nickname', 'age', 'dress_size', 'shoe_size', 'shirt_size', 'pant_size', 'underwear_or_diaper_size', 'sock_size')