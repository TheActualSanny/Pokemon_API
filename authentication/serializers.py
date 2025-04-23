from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(max_length = 150)

    def validate(self, attrs):
        if not attrs.get('password') == attrs.get('password_confirm'):
            raise ValueError('Make sure that the password match!')
        return attrs
    
    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm']

class LoginSerializer(serializers.Serializer):
    '''
        Sole purpose of this serializer class is to make sure that
        the user passed the username and password fields.
        This helps us avoid additional checks in views.
    '''
    username = serializers.CharField()
    password = serializers.CharField()
