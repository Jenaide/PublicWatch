from .models import User, MostWanted, MissingPerson
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class MostWantedSerializer(serializers.ModelSerializer):
    class Meta:
        model = MostWanted
        fields = '__all__'

class MissingPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissingPerson
        fields = '__all__'
