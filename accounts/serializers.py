from rest_framework import serializers
from .models import User, Album, Band, Genre


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password', 'groups',
                  'user_permissions', 'is_staff', 'is_active',
                  'is_superuser', 'last_login', 'date_joined')

    # create a user below 
    def create(self, valid_data):
        user = User.objects.create( 
        username=valid_data['username'],
        password=valid_data['password'],)
        return user
