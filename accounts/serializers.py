from rest_framework import serializers
from .models import User, Album, Band, Genre


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user', 'genres', 'albums', 'bands')

