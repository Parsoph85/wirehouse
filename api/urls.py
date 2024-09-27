from django.urls import path

from api.views import UserModelViewSet, WarehouseModelViewSet, WarehouseCreateView, UserRegistrationView, UserLoginView, \
    ProductViewSet, ProductCreateView, ProductRetrieveView

urlpatterns = [
    #path('api-auth/', include('rest_framework.urls')),
]
