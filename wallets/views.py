from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated

from wallets.models import Wallet, OperationType
from wallets.serializers import WalletsSerializer, OperTypeSerializer


class WalletOwnerUpdate(permissions.BasePermission):
    """Права доступа на чтение и запись"""

    def has_object_permission(self, request, view, obj):
        # Разрешаем чтение и запись только владельцу или админу
        return obj.owner == request.user or request.user.is_staff


class WalletsDetailApiView(generics.RetrieveAPIView):
    """Подробное описание"""

    serializer_class = WalletsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Пользователь видит только свои кошельки, админ - все
        if self.request.user.is_staff:
            return Wallet.objects.all()
        return Wallet.objects.filter(owner=self.request.user)


class WalletsBalanceApiUpdate(generics.UpdateAPIView):
    """Редактирование описания"""

    queryset = Wallet.objects.all()
    serializer_class = WalletsSerializer
    permission_classes = [IsAuthenticated, WalletOwnerUpdate]


class WalletView(generics.ListAPIView):
    """Просмотр списка кошельков"""

    queryset = Wallet.objects.all()
    serializer_class = WalletsSerializer


class CreateWallet(generics.CreateAPIView):
    """Создание кошелька"""

    queryset = Wallet.objects.all()
    serializer_class = WalletsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CreateType(generics.CreateAPIView):
    """Создание типа операции"""

    queryset = OperationType.objects.all()
    serializer_class = OperTypeSerializer


class TypeView(generics.ListAPIView):
    """Просмотр списка типов операций"""

    queryset = OperationType.objects.all()
    serializer_class = OperTypeSerializer
