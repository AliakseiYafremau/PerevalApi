from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response

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

    # переписывание get_queryset для фильтрации по email
    def get_queryset(self):
        queryset = super().get_queryset()

        user_email = self.request.query_params.get('user__email')
        print(user_email)
        if user_email:
            print('email')
            return PerevalAdded.objects.filter(user__email=user_email)
        print('not')
        return queryset


class PerevalAddedUpdateView(generics.RetrieveUpdateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedUpdateSerializer

    # переписывание UpdateModelMixin-а, который сохраняет обьект
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        is_serializer_valid = serializer.is_valid()
        if is_serializer_valid:
            serializer.save()
            return Response({'state': 1, 'message': 'Запись успешно обновлена'})
        else:
            return Response({'state': 0, 'message': serializer.errors})