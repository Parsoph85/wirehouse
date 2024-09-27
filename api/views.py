from rest_framework import viewsets, generics, permissions, serializers
from api.models import ApiUser, Warehouse, Product
from api.serializers import UserSerializer, WarehouseSerializer, ProductSerializer, LoginSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from api.permissions import IsSupply, IsConsumer



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
    queryset = ApiUser.objects.all()
    serializer_class = LoginSerializer

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


class WarehouseCreateView(generics.CreateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [IsSupply]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsSupply]


class ProductRetrieveView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsConsumer]

    def perform_update(self, serializer):
        quantity_to_retrieve = self.request.data.get('quantity')
        if quantity_to_retrieve > serializer.instance.quantity:
            raise serializers.ValidationError("Нельзя забрать больше, чем " + str(serializer.instance.quantity))
        serializer.save(quantity=serializer.instance.quantity - quantity_to_retrieve)