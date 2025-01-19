from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

User = get_user_model()


# Create your tests here.
class SignupAPIViewTestCase(APITestCase):
    def test_signup(self):
        url = reverse("signup")
        user_data = {
            "username": "JIN HO",
            "password": "12341234",
            "nickname": "Mentos",
        }
        response = self.client.post(url, user_data)
        print("signup response: ", response.data)
        # 상태 코드 검증
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LoginAPIViewTestCase(APITestCase):
    def setUp(self):
        self.data = {
            "username": "JIN HO",
            "password": "12341234",
        }
        User.objects.create_user(
            username="JIN HO", password="12341234", nickname="Mentos"
        )

    def test_login(self):
        url = reverse("login")
        response = self.client.post(url, self.data)
        print("login response", response.data)
        # 상태 코드 검증
        self.assertEqual(response.status_code, status.HTTP_200_OK)
