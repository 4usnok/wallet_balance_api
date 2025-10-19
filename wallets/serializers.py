from rest_framework import serializers
from wallets.models import Wallet, OperationType


class OperTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = OperationType
        fields = ["id", "name_oper"]


class WalletsSerializer(serializers.ModelSerializer):
    operation_type = serializers.SlugRelatedField(
        slug_field="name_oper", source="oper_type", queryset=OperationType.objects.all()
    )

    class Meta:
        model = Wallet
        fields = ["operation_type", "amount"]
