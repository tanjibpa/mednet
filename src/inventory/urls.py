from django.urls import path

from inventory.views import ProductsListView, ProductCreateView

app_name = 'inventory'
urlpatterns = [
    path('list', ProductsListView.as_view(), name='product_list_view'),
    path('create', ProductCreateView.as_view(), name='product_create_view')
]
