from django.contrib import admin
from .models import PerevalAdded, User, Coords, Level, PerevalImage

# Регистрация Моделей в админ панели
admin.site.register(PerevalAdded)
admin.site.register(User)
admin.site.register(Coords)
admin.site.register(Level)
admin.site.register(PerevalImage)
