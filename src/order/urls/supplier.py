from django.urls import path

from order.views import SupplierOrderListView

app_name = 'supplier_order'
urlpatterns = [
    path('list', SupplierOrderListView.as_view(), name='order_list_view'),
]
