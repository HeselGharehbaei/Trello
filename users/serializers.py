from rest_framework import serializers
from .models import User


class UserBriefSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ("id", "username", "first_name", 
                  "last_name", "email", 
                  "image", 
        )


class UserDetailSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields =  '__all__'
