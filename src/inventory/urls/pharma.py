from django.urls import path

from inventory.views import (
    PharmaProductsListView,
    PharmaProductCreateView,
    PharmaProductDetailView,
    PharmaProductUpdateView,
    PharmaRawMaterialDetailView,
    PharmaRawMaterialListView
)

app_name = 'pharma_inventory'
urlpatterns = [
    path('list', PharmaProductsListView.as_view(), name='product_list_view'),
    path('create', PharmaProductCreateView.as_view(), name='product_create_view'),
    path('detail/<int:pk>', PharmaProductDetailView.as_view(), name='product_detail_view'),
    path('update/<int:pk>', PharmaProductUpdateView.as_view(), name='product_update_view'),
    path('raw_material/<int:pk>', PharmaRawMaterialDetailView.as_view(), name='raw_material_detail_view'),
    path('raw_material', PharmaRawMaterialListView.as_view(), name='raw_material_list_view'),
]
