from django.urls import path

from .views import WalletOperationView, WalletsDetailApiView

app_name = "wallets"

urlpatterns = [
    path("<uuid:id>/", WalletsDetailApiView.as_view(), name="wallets_balance"),
    path(
        "<uuid:id>/operation/", WalletOperationView.as_view(), name="wallets-operation"
    ),
]
