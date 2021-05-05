from django.urls import path

from inventory.views.supplier import (
    SupplierRawMaterialListView,
    SupplierRawMaterialCreateView,
    SupplierRawMaterialDetailView,
    SupplierRawMaterialUpdateView,
)

app_name = "supplier_inventory"
urlpatterns = [
    path("list", SupplierRawMaterialListView.as_view(), name="raw_material_list_view"),
    path(
        "create",
        SupplierRawMaterialCreateView.as_view(),
        name="raw_material_create_view",
    ),
    path(
        "detail/<int:pk>",
        SupplierRawMaterialDetailView.as_view(),
        name="raw_material_detail_view",
    ),
    path(
        "edit/<int:pk>",
        SupplierRawMaterialUpdateView.as_view(),
        name="raw_material_update_view",
    ),
]
