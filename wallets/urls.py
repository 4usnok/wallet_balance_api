from django.urls import path

from .views import (
    WalletsBalanceApiUpdate,
    WalletsDetailApiView,
    CreateType,
    TypeView,
    WalletView,
    CreateWallet,
)

app_name = "wallets"

urlpatterns = [
    path("view_type/", TypeView.as_view(), name="view_type"),
    path("view_wallet/", WalletView.as_view(), name="view_wallet"),
    path("create_wallet/", CreateWallet.as_view(), name="create_wallet"),
    path("create_type/", CreateType.as_view(), name="create_type"),
    path("<int:pk>/", WalletsDetailApiView.as_view(), name="wallets_balance"),
    path(
        "<int:pk>/operation/", WalletsBalanceApiUpdate.as_view(), name="wallets-update"
    ),
]
