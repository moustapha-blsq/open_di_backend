from rest_framework import serializers
from rest_framework.views import APIView
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nom_complet', 'email', 'password']
        #Hide the password for responses


#Hashing password
class RegisterView(APIView):
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None :
            instance.set_password(password)
        instance.save()
        return instance

#Define fonction for authentification


