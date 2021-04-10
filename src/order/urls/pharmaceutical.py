from django.urls import path

from order.views import PharmaceuticalOrderCreateView

app_name = 'pharmaceutical_order'
urlpatterns = [
    path('<int:product_id>/create', PharmaceuticalOrderCreateView.as_view(), name='order_create_view'),
]
