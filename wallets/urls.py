from django.urls import path

from .views import WalletsBalanceApiUpdate, WalletsDetailApiView

app_name = "wallets"

urlpatterns = [
    path("<int:pk>/", WalletsDetailApiView.as_view(), name="wallets_balance"),
    path(
        "<int:pk>/operation/", WalletsBalanceApiUpdate.as_view(), name="wallets-update"
    ),
]
