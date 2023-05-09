from django.contrib.auth import get_user_model
from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.permissions import IsAdminUser

#serializer

class CustomRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    department = serializers.CharField()
    year = serializers.IntegerField()
    block = serializers.CharField()
    room = serializers.CharField()
    bed = serializers.CharField()
   
    def save(self, *args):
        user = CustomUser(
            email=self.validated_data['email'],
            department=self.validated_data['department'],
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            year=self.validated_data['year'],
            block=self.validated_data['block'],
            room=self.validated_data['room'],
            bed=self.validated_data['bed'],
        )
        user.save()
        return user


#serializers.py file

User = get_user_model()

class CustomLoginSerializer(LoginSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, style={'input_type': 'password'})
    
    def authenticate(self, **kwargs):
        username = kwargs['username']
        password = kwargs['password']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid username or password')

        if not user.check_password(password):
            raise serializers.ValidationError('Invalid username or password')

        return user

    def get_fields(self):
        fields = super().get_fields()
        fields.pop('email', None)  # Remove email field
        fields['username'] = serializers.CharField(
            required=True,
            style={'input_type': 'text'} 
        )
        return fields




