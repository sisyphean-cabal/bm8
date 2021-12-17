from rest_framework import serializers
from accounts.models import User
from rest_framework.validators import UniqueValidator

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password', 'groups',
                  'user_permissions', 'is_staff', 'is_active',
                  'is_superuser', 'last_login', 'date_joined')

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password_confirmation = serializers.CharField(max_length=280)
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'passwordConfirmation']
        extra_kwargs = {
            'password': {'write_only': True}
        }

        

    def save(self):
        account = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']

        account.set_password(password)
        account.save()
        return account

    