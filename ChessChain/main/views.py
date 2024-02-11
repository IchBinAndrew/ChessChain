from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Room
from django.forms import model_to_dict
from .serializers import RoomSerializer

# Create your views here.
class RoomAPIView(APIView):
    def get(self, request):
        srlz = Room.objects.all()
        return Response({'info': RoomSerializer(srlz, many=True).data})

    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PATCH is not allowed"})

        try:
            instance = Room.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = RoomSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        return Response({"post": "delete_post"} + str(pk))

# Create your views here.
def index(request):
    return render(request, 'main/index.html')