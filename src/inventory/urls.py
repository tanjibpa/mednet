from django.urls import path

from inventory.views import ProductsListView, ProductCreateView, ProductDetailView, ProductUpdateView

app_name = 'inventory'
urlpatterns = [
    path('list', ProductsListView.as_view(), name='product_list_view'),
    path('create', ProductCreateView.as_view(), name='product_create_view'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='product_detail_view'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='product_update_view'),
]
