from rest_framework import serializers
from .models import User
from workspaces.models import Workspace


class UserWorkspacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = ['id', 'title']


class UserBriefSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ("id", "username", "first_name", 
                  "last_name", "email", 
                  "image", 
        )


class UserDetailSerializer(serializers.ModelSerializer):
    user_owned_workspaces = UserWorkspacesSerializer(
        many= True, 
        source= "get_user_owned_workspace", 
        read_only = True,
    )
    user_membered_workspaces = UserWorkspacesSerializer(
        many= True, 
        source= "get_user_membered_workspaces", 
        read_only = True,
    )


    class Meta:
        model = User
        fields =  '__all__'
