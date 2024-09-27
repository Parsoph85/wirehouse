from django.urls import path

from api.views import UserModelViewSet, WarehouseModelViewSet, WarehouseCreateView, UserRegistrationView, UserLoginView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('users/', UserModelViewSet.as_view({'get': 'list'}), name='user-list'),
    path('warehouses/', WarehouseModelViewSet.as_view({'get': 'list'}), name='warehouses'),
    path('api-auth/', include('rest_framework.urls')),
    path('createwh/', WarehouseCreateView.as_view(), name='create_warehouse'),
]