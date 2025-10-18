from rest_framework import serializers

from wallets.models import Wallet


class WalletsSerializer(serializers.ModelSerializer):
    operation_type = serializers.SlugRelatedField(
        source="oper_type", slug_field="name_oper", read_only=True
    )

    class Meta:
        model = Wallet
        fields = ["operation_type", "amount"]
