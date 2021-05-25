from django.urls import path

from inventory.views import RetailerProductList, RetailerProductDetail

app_name = "retailer_inventory"

urlpatterns = [
    path("list", RetailerProductList.as_view(), name="product_list_view"),
    path(
        "detail/<int:pk>", RetailerProductDetail.as_view(), name="product_detail_view"
    ),
]
