from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from wallets.models import OperationType, Wallet


class WalletsApiTestCase(APITestCase):
    def setUp(self):
        """Подготовка данных перед каждым тестом"""
        self.user = User.objects.create_user(  # создание пользователя
            username="testuser",
            password="testpass123",
            email="test@example.com"
        )
        self.client.force_authenticate(user=self.user)  # авторизация

        self.operation_type = (  # создание данных типа операции
            OperationType.objects.create(
                name_oper="test_name",
            )
        )
        self.wallets = Wallet.objects.create(  # создание данных кошелька
            owner=self.user,
            oper_type=self.operation_type,
            amount=10,
        )

    def test_list_view_wallets(self):
        """Тестирование просмотра баланса"""
        urls_from_detail = reverse(
            "wallets:wallets_balance", kwargs={"pk": self.wallets.pk}
        )

        response = self.client.get(urls_from_detail, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_view_wallets(self):
        """Тестирование редактирования кошелька"""
        data_from_update = {
            "oper_type": "test_type",
            "amount": 100
        }
        urls_create = reverse(
            "wallets:wallets-update", kwargs={"pk": self.wallets.pk}
        )

        response = self.client.patch(urls_create, data=data_from_update, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
