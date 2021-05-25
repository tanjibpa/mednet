from django.urls import path

from order.views import RetailerOrderProduct

app_name = "retailer_order"

urlpatterns = [
    path("create", RetailerOrderProduct.as_view(), name="order_create_view")]
