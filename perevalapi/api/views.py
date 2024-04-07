from django.shortcuts import render
from rest_framework import viewsets

from .models import Pereval, User, Cords, Level
from .serializers import PerevalSerializer, UserSerializer, CordsSerializer, LevelSerializer


# Create your views here.
class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CordsViewSet(viewsets.ModelViewSet):
    queryset = Cords.objects.all()
    serializer_class = CordsSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
