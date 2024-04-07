from django.shortcuts import render
from rest_framework import viewsets

from .models import PerevalAdded, User, Coords, Level
from .serializers import PerevalAddedSerializer, UserSerializer, CoordsSerializer, LevelSerializer


# Create your views here.
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
