from django.contrib.auth.models import User
from django.db import models


class OperationType(models.Model):
    """Модель для типов операций"""

    name_oper = models.CharField(
        max_length=25, help_text="Введите название типа операции"
    )

    def __str__(self):
        return self.name_oper


class Wallet(models.Model):
    """Модель для кошелька"""

    owner = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Владелец")
    oper_type = models.ForeignKey(
        OperationType,
        on_delete=models.CASCADE,
        help_text="Выберите тип операции",
    )
    amount = models.IntegerField(help_text="Введите сумму баланса кошелька")

    def __str__(self):
        return self.oper_type
