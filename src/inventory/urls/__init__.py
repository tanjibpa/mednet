from django.urls import path, include

urlpatterns = [
    path('pharma/', include('inventory.urls.pharma', namespace='pharma_inventory')),
    path('supplier/', include('inventory.urls.supplier', namespace='supplier_inventory')),
]
