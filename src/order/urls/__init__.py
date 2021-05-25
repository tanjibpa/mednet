from django.urls import include, path

urlpatterns = [
    path("supplier/", include("order.urls.supplier", namespace="supplier_order")),
    path(
        "pharmaceutical/",
        include("order.urls.pharmaceutical", namespace="pharmaceutical_order"),
    ),
    path("retailer/", include("order.urls.retailer", namespace="retailer_order")),
]
