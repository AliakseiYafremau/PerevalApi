from rest_framework import serializers

from .models import PerevalAdded, User, Coords, Level, PerevalImage


# Создание сериализера
class PerevalAddedSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class PerevalImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImage
        fields = '__all__'


class PerevalAddedUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalAdded
        exclude = ['user']
