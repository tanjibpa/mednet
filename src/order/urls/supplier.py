from django.urls import path

from order.views import SupplierOrderListView, SupplierOrderFulfillView, SupplierOrderRejectView

app_name = 'supplier_order'
urlpatterns = [
    path('list', SupplierOrderListView.as_view(), name='order_list_view'),
    path('fulfill/<int:order_id>', SupplierOrderFulfillView.as_view(), name='order_fulfill_view'),
    path('reject/<int:order_id>', SupplierOrderRejectView.as_view(), name='order_reject_view'),
]
