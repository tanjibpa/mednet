from django.urls import path

from order.views import PharmaceuticalRawMaterialOrderCreateView, PharmaceuticalRawMaterialOrderListView

app_name = 'pharmaceutical_order'
urlpatterns = [
    path('create', PharmaceuticalRawMaterialOrderCreateView.as_view(), name='order_create_view'),
    path('list', PharmaceuticalRawMaterialOrderListView.as_view(), name='order_list_view'),
]
