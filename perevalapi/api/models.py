from django.db import models


# Модель пользователя
class User(models.Model):
    email = models.EmailField(unique=True)
    fam = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    otc = models.CharField(max_length=25)
    phone = models.CharField(max_length=17, null=True, blank=True)

    def __str__(self):
        return f'{self.email} | {self.fam} | {self.name}'


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
class PerevalAdded(models.Model):

    STATUS = [
        ('new', 'новый'),
        ('pending', 'в работе'),
        ('accepted', 'принят'),
        ('rejected', 'отклонен')
    ]

    beauty_title = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    other_titles = models.CharField(max_length=50)
    connect = models.CharField(max_length=20, default="")
    status = models.CharField(max_length=50, choices=STATUS, default='new')
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = models.ForeignKey(Coords, on_delete=models.PROTECT)
    level = models.ForeignKey(Level, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.title} | {self.pk}'


# Модель фотографий
class PerevalImage(models.Model):
    pereval = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE)
    # TODO удостовериться на счет типа поля
    image = models.ImageField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Image | {self.pereval.title} | {self.pk}'
