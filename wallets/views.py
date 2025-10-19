from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from wallets.models import Wallet
from wallets.serializers import WalletSerializer, OperationSerializer


class WalletOwner(permissions.BasePermission):
    """Права доступа на чтение и запись"""

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user or request.user.is_staff


class WalletsDetailApiView(generics.RetrieveAPIView):
    """Баланс кошелька"""

    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated, WalletOwner]
    lookup_field = 'id'

    def get_queryset(self):
        # Пользователь видит только свои кошельки, админ - все
        if self.request.user.is_staff:
            return Wallet.objects.all()
        return Wallet.objects.filter(owner=self.request.user)

class WalletOperationView(generics.RetrieveAPIView):
    """Операции с балансом"""

    serializer_class = WalletSerializer
    permission_classes = [permissions.IsAuthenticated, WalletOwner]
    lookup_field = 'id'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Wallet.objects.all()
        return Wallet.objects.filter(owner=self.request.user)

    def post(self, request, *args, **kwargs):

        wallet = self.get_object()

        serializer = OperationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        operation_type = serializer.validated_data['operation_type']
        amount = serializer.validated_data['amount']

        if operation_type == 'DEPOSIT':
            wallet.balance += amount

        elif operation_type == 'WITHDRAW':
            if wallet.balance < amount:
                return Response(
                    {'error': 'Insufficient funds'},
                    status=400
                )
            wallet.balance -= amount

        wallet.save()

        return Response(WalletSerializer(wallet).data)
