from rest_framework import serializers, validators
from api.models import ApiUser, Warehouse, Product


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128, validators=[
        validators.UniqueValidator(ApiUser.objects.all())], label='Логин')
    email = serializers.EmailField(validators=[
        validators.UniqueValidator(ApiUser.objects.all())], label='E-mail')
    password = serializers.CharField(min_length=6, max_length=20, write_only=True, label='Пароль')
    user_type = serializers.BooleanField(label='Поставщик')

    def update(self, instance, validated_data):
        if email := validated_data.get("email"):
            instance.email = email
            instance.save(update_fields=["email"])

        if password := validated_data.get("password"):
            instance.set_password(password)
            instance.save(update_fields=["password"])
        return instance

    def create(self, validated_data):
        user = ApiUser.objects.create(
            email=validated_data["email"],
            username=validated_data["username"],
            user_type=validated_data["user_type"],
        )

        user.set_password(validated_data["password"])
        user.save(update_fields=["password"])
        return user


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

    def validate(self, data):
        quantity_to_retrieve = self.context['request'].data.get('quantity')
        if quantity_to_retrieve > data['quantity']:
            raise serializers.ValidationError("Cannot retrieve more than available quantity.")
        return data

