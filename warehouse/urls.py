from django.contrib import admin
from django.urls import path

from api.views import UserModelViewSet, WarehouseCreateView, UserRegistrationView, UserLoginView, \
    ProductViewSet, ProductCreateView, ProductRetrieveView, WarehouseModelViewSet

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', UserLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('users/', UserModelViewSet.as_view({'get': 'list'}), name='user-list'),
    path('createwh/', WarehouseCreateView.as_view(), name='create_warehouse'),
    path('warehouses/', WarehouseModelViewSet.as_view({'get': 'list'}), name='warehouses-list'),
    path('products/', ProductViewSet.as_view({'get': 'list'}), name='product-list'),
    path('products/add/', ProductCreateView.as_view(), name='create_prod'),
    path('products/take/<int:pk>/', ProductRetrieveView.as_view(), name='retriv_prod'),
]
