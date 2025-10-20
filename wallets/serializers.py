from rest_framework import serializers

from .models import OperationType, Wallet


class OperationSerializer(serializers.Serializer):
    operation_type = serializers.ChoiceField(choices=OperationType)
    amount = serializers.DecimalField(max_digits=15, decimal_places=2, min_value=0.01)


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ["id", "balance"]
