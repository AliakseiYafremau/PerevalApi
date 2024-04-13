from rest_framework import viewsets
from rest_framework import generics

from .models import PerevalAdded, User, Coords, Level, PerevalImage
from .serializers import *


# Создание представлений набора
class PerevalAddedViewSet(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CoordsViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class PerevalImageViewSet(viewsets.ModelViewSet):
    queryset = PerevalImage.objects.all()
    serializer_class = PerevalImageSerializer


class PerevalAddedPostView(generics.ListCreateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer


class PerevalAddedUpdateView(generics.RetrieveUpdateAPIView,):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedUpdateSerializer
