import uuid

from django.contrib.auth.models import User
from django.db import models


class OperationType(models.TextChoices):
    """Модель для типа транзакции"""

    DEPOSIT = "DEPOSIT", "Deposit"
    WITHDRAW = "WITHDRAW", "Withdraw"


class Wallet(models.Model):
    """Модель для кошелька"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Владелец")
    balance = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00, help_text="Текущий баланс"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Wallet {self.id} - Balance: {self.balance}"
