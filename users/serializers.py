from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для модели пользователя"""

    class Meta:
        model = User
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра профиля пользователя"""

    class Meta:
        model = User
        fields = '__all__'