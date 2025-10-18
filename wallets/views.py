from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated

from wallets.models import Wallet
from wallets.serializers import WalletsSerializer


class WalletOwnerUpdate(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Разрешаем чтение и запись только владельцу или админу
        return obj.owner == request.user or request.user.is_staff


class WalletsDetailApiView(generics.RetrieveAPIView):
    serializer_class = WalletsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Пользователь видит только свои кошельки, админ - все
        if self.request.user.is_staff:
            return Wallet.objects.all()
        return Wallet.objects.filter(owner=self.request.user)


class WalletsBalanceApiUpdate(generics.UpdateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletsSerializer
    permission_classes = [IsAuthenticated, WalletOwnerUpdate]
