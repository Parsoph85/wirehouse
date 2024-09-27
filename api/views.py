from rest_framework import viewsets, permissions, generics
from rest_framework.generics import get_object_or_404
from api.models import ApiUser, Warehouse
from api.serializers import UserSerializer, WarehouseSerializer, ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class UserRegistrationView(generics.CreateAPIView):
    queryset = ApiUser.objects.all()
    serializer_class = UserSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    http_method_names = ['post', 'get']
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = []


class UserLoginView(generics.GenericAPIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Введены некорректные данные'}, status=400)


class WarehouseModelViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

    @action(detail=True)
    def products(self, request, pk=None):
        warehouse = get_object_or_404(Warehouse.objects.all(), id=pk)
        prod_list = warehouse.product.filter(quantity__isnull=True)
        return Response(
            ProductSerializer(prod_list, many=True).data
        )


class WarehouseCreateView(generics.CreateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [permissions.IsAuthenticated]
