from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('organization/', include('organization.urls')),
    path('inventory/', include('inventory.urls')),
]
