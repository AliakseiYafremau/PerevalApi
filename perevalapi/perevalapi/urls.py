"""
URL configuration for perevalapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api import views

# регистрация роутера с моделями
router = routers.DefaultRouter()
router.register(r'perevals', views.PerevalAddedViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'coords', views.CoordsViewSet)
router.register(r'levels', views.LevelViewSet)
router.register(r'images', views.PerevalImageViewSet)

# url паттерны
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    # метод пост для создания перевала
    path('submitData/', views.PerevalAddedPostView.as_view()),
    path('submitData/<int:pk>/', views.PerevalAddedUpdateView.as_view()),
]
