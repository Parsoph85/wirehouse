from rest_framework import serializers, validators
from api.models import ApiUser, Warehouse, Product


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128, validators=[
        validators.UniqueValidator(ApiUser.objects.all())], label='Логин')
    email = serializers.EmailField(validators=[
        validators.UniqueValidator(ApiUser.objects.all())], label='E-mail')
    password = serializers.CharField(min_length=6, max_length=20, write_only=True, label='Пароль')
    user_type = serializers.BooleanField(label='Поставщик')

    def create(self, validated_data):
        user = ApiUser.objects.create(
            email=validated_data["email"],
            username=validated_data["username"],
            user_type=validated_data["user_type"],
        )
        user.set_password(validated_data["password"])
        user.save(update_fields=["password"])
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128, validators=[
        validators.UniqueValidator(ApiUser.objects.all())], label='Логин')
    password = serializers.CharField(min_length=6, max_length=20, write_only=True, label='Пароль')


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}

