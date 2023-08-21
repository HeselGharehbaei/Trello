from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    user_owned_workspaces = serializers.StringRelatedField(many= True, source= "get_user_owned_workspace")
    user_membered_workspaces = serializers.StringRelatedField(many= True, source= "get_user_membered_workspaces")

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "image", "user_owned_workspaces", "user_membered_workspaces")
