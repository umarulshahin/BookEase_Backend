from rest_framework import serializers
from .models import *
import re


#............................................Registration serializer............................................
class RegistrationSerializer(serializers.ModelSerializer):
    
    con_password = serializers.CharField(write_only=True)
    class Meta: 
        model = CustomUser
        fields = ['email', 'username', 'password', 'con_password']
        read_only_fields = ['user_id']
        extra_kwargs = {'con_password' : {'write_only': True}}
        
    #........................ validation for email, username and password........................
    def validate(self, attrs):
        
        username_pattern = r'^(?!\s+$)[A-Za-z][A-Za-z0-9_ ]{2,}$'
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        password_pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$'
        
        if not re.match(username_pattern, attrs['username']):
            raise serializers.ValidationError({'error':'Invalid Username.Username must contain atleast 4 characters and must start with a letter'})
        
        if CustomUser.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError({'error':'Username already exists'})
        
        if not re.match(email_pattern, attrs['email']):
            raise serializers.ValidationError({'error':'Invalid Email format'})
        
        if CustomUser.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({'error':'Email already exists'})
        
        if not re.match(password_pattern, attrs['password']): 
            raise serializers.ValidationError({'error':'Invalid Password . Password must contain atleast 8 characters, 1 uppercase, 1 digit and 1 special character'})
        
        if attrs['password'] != attrs['con_password']:
            raise serializers.ValidationError({'error':'Password does not match'})
        return attrs
    
    #........................ creating user........................
    def create(self, validated_data):
        
        user = CustomUser.objects.create_user(email=validated_data['email'], 
                                              username=validated_data['username'],
                                              password=validated_data['password'])
        user.save()
        return user