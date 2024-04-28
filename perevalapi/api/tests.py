from django.test import TestCase
from api import models

class RESTAPITest(TestCase):
    def setUp(self):
        testLevel1 = models.Level.objects.create(
            winter='A1',
            spring='B2',
            summer='C3',
            autumn='D4',
        )

        testLevel2 = models.Level.objects.create(
            winter='D4',
            spring='C3',
            summer='B2',
            autumn='A1',
        )

        testCoords = models.Coords.objects.create(
            latitude = 1234.56789,
            longitude = 9876.54321,
            height = 1000,
        )

        testUser1 = models.User.objects.create(
            email='ivaivaiva@mail.ru',
            fam='Ivanov',
            name='Ivan',
            otc='Ivanovich',
            phone='123456789'
        )

        testUser2 = models.User.objects.create(
            email='alealeale@mail.ru',
            fam='Alekseev',
            name='Aleksei',
            otc='Alekseevich',
            phone='987654321'
        )