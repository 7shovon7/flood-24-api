from typing import Any, Dict
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as BaseTokenObtainPairSerializer

# from .models import Customer, ProductManager


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'email', 'password', 'phone', 'full_name']

    # def create(self, validated_data):
    #     user = super().create(validated_data)
    #     user_role = validated_data.get('user_role')
        
    #     profile_class = None
    #     if user_role == settings.K_MANAGER_USER_ROLE:
    #         profile_class = ProductManager
    #     elif user_role == settings.K_CUSTOMER_USER_ROLE:
    #         profile_class = Customer
    #     # Create the associated user profile based on role
    #     if profile_class is not None:
    #         profile_class.objects.create(user=user)
        
    #     return user


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'email', 'phone', 'full_name']


class TokenObtainPairSerializer(BaseTokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        token['id'] = user.id
        token['email'] = user.email
        token['phone'] = user.phone
        token['full_name'] = user.full_name
        # token['user_role'] = user.user_role
        
        return token
    
    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)
        
        data["id"] = self.user.id
        data["email"] = self.user.email
        data["phone"] = self.user.phone
        data["full_name"] = self.user.full_name
        # data["user_role"] = self.user.user_role
        
        return data
