from django.db import models
from django.contrib.auth.models import User


# Модель координат перевала
class Coords(models.Model):
    latitude = models.DecimalField(max_digits=12, decimal_places=4)
    longitude = models.DecimalField(max_digits=12, decimal_places=4)
    height = models.IntegerField()

    def __str__(self):
        return f'{self.latitude} | {self.longitude} | {self.height}'


# Модель уровня перевала
class Level(models.Model):
    winter = models.CharField(max_length=25)
    spring = models.CharField(max_length=25)
    summer = models.CharField(max_length=25)
    autumn = models.CharField(max_length=25)

    def __str__(self):
        return f'Wi: {self.winter} | Sp: {self.spring} | Su: {self.summer} | Au: {self.autumn}'


# Модель перевала
class Pereval(models.Model):
    beauty_title = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    other_titles = models.CharField(max_length=50)
    connect = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = models.OneToOneField(Coords, on_delete=models.PROTECT)
    level = models.OneToOneField(Level, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.title} | {self.pk}'


class Image(models.Model):
    data = models.ImageField()
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE)

    def __str__(self):
        return f'Image | {self.pereval.title } | {self.pk}'
