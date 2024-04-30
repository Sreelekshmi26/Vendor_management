from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
#     path('vendors/<int:pk>/', VendorRetrieveUpdateDeleteView.as_view(), name='vendor-retrieve-update-delete'),
#     path('purchase_orders/', PurchaseListCreateView.as_view(), name='purchase-list-create'),
#     path('purchase_orders/<int:pk>/', PurchaseRetrieveUpdateDeleteView.as_view(), name='purchase-retrieve-update-delete'),
# ]
router = DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'purchase_orders', PurchaseOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]