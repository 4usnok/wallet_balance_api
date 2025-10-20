from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from wallets.models import Wallet


class WalletsApiTestCase(APITestCase):
    def setUp(self):
        """Подготовка данных перед каждым тестом"""
        self.user = User.objects.create_user(  # создание пользователя
            username="testuser", password="testpass123", email="test@example.com"
        )
        self.client.force_authenticate(user=self.user)  # авторизация

        self.wallets = Wallet.objects.create(  # создание данных кошелька
            balance=1500.00, owner=self.user
        )

    def test_wallets_detail_api_view(self):
        """Тестирование просмотра баланса кошелька"""
        urls_from_detail = reverse(
            "wallets:wallets_balance", kwargs={"id": self.wallets.id}
        )

        response = self.client.get(urls_from_detail, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deposit_operation_success(self):
        """Пополнение счета"""
        url = f"/api/v1/wallets/{self.wallets.id}/operation/"
        data = {"operation_type": "DEPOSIT", "amount": "500.00"}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["balance"], "2000.00")

    def test_deposit_operation_negative_amount(self):
        """Снятие со счёта"""
        url = f"/api/v1/wallets/{self.wallets.id}/operation/"
        data = {"operation_type": "WITHDRAW", "amount": "500.00"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["balance"], "1000.00")
