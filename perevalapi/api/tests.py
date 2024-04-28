from django.test import RequestFactory, TestCase
from .views import PerevalAddedViewSet, CoordsViewSet, LevelViewSet, UserViewSet


class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_details(self):
        # Создаем словари обьектов
        coords1 = {
            "latitude": 1234.5678,
            "longitude": 9876.4321,
            "height": 1000,
        }
        coords2 = {
            "latitude": 9876.4321,
            "longitude": 1234.5678,
            "height": 2000,
        }
        level1 = {
            "winter": "A1",
            "spring": "B2",
            "summer": "C3",
            "autumn": "D4",
        }
        level2 = {
            "winter": "D4",
            "spring": "C3",
            "summer": "B2",
            "autumn": "A1",
        }
        user1 = {
            "email": "ivaivaiva@mail.ru",
            "fam": "Ivanov",
            "name": "Ivan",
            "otc": "Ivanovich",
            "phone": "+123456789",
        }

        user2 = {
            "email": "alalala@mail.ru",
            "fam": "Alex",
            "name": "Alex",
            "otc": "Alexeevich",
            "phone": "+123456789",
        }

        pereval1 = {
            "beauty_title": "Beauty title",
            "title": "Title",
            "other_titles": "Another title",
            "connect": "CONNECT",
            "status": "new",
            "user": 1,
            "coords": 1,
            "level": 1
        }

        # Создаем инстанты запросов
        coords1_request_post = self.factory.post("coords", data=coords1, format="json")
        coords2_request_post = self.factory.post("coords", data=coords2, format="json")

        level1_request_post = self.factory.post("levels", data=level1, format="json")
        level2_request_post = self.factory.post("levels", data=level2, format="json")

        user1_request_post = self.factory.post("users", data=user1, format="json")
        user2_request_post = self.factory.post("users", data=user2, format="json")

        pereval1_request_post = self.factory.post("perevals", data=pereval1, format="json")

        coords_request_get = self.factory.get("coords", format="json")
        level_request_get = self.factory.get("level", format="json")
        user_request_get = self.factory.get("users", format="json")
        pereval1_request_get = self.factory.get("perevals", format="json")

        # Делаем запрос
        coords1_response_post = CoordsViewSet.as_view({'post': 'create'})(coords1_request_post)
        coords2_response_post = CoordsViewSet.as_view({'post': 'create'})(coords2_request_post)

        level1_response_post = LevelViewSet.as_view({'post': 'create'})(level1_request_post)
        level2_response_post = LevelViewSet.as_view({'post': 'create'})(level2_request_post)

        user1_response_post = UserViewSet.as_view({'post': 'create'})(user1_request_post)
        user2_response_post = UserViewSet.as_view({'post': 'create'})(user2_request_post)

        pereval1_response_post = PerevalAddedViewSet.as_view({'post': 'create'})(pereval1_request_post)

        coords_response_get = CoordsViewSet.as_view({'get': 'list'})(coords_request_get)
        level_response_get = LevelViewSet.as_view({'get': 'list'})(level_request_get)
        user_response_get = UserViewSet.as_view({'get': 'list'})(user_request_get)
        pereval_response_get = UserViewSet.as_view({'get': 'list'})(pereval1_request_get)

        #print(coords1_response_post.data)
        #print(coords2_response_post.data)

        #print(level1_response_post.data)
        #print(level2_response_post.data)

        #print(user1_response_post.data)
        #print(user2_response_post.data)

        #print(pereval1_response_post.data)

        #print(coords_response_get.data)
        #print(level_response_get.data)
        #print(user_response_get.data)
        #print(pereval_response_get.data)

        self.assertEqual(coords1_response_post.status_code, 201)
        self.assertEqual(coords2_response_post.status_code, 201)
        self.assertEqual(coords_response_get.status_code, 200)

        self.assertEqual(level1_response_post.status_code, 201)
        self.assertEqual(level2_response_post.status_code, 201)
        self.assertEqual(level_response_get.status_code, 200)

        self.assertEqual(user1_response_post.status_code, 201)
        self.assertEqual(user2_response_post.status_code, 201)
        self.assertEqual(user_response_get.status_code, 200)

        self.assertEqual(pereval1_response_post.status_code, 201)
        self.assertEqual(pereval_response_get.status_code, 200)

