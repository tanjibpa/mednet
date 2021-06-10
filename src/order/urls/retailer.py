from django.urls import path

from order.views import RetailerOrderProduct, RetailerOrderListView

app_name = "retailer_order"

urlpatterns = [
    path("create", RetailerOrderProduct.as_view(), name="order_create_view"),
    path("list", RetailerOrderListView.as_view(), name="order_list_view")
]
