from rest_framework import serializers
from .models import User
from workspaces.models import Workspace
from boards.models import Task    


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


class CompletedTaskSerializer(serializers.ModelSerializer):


    class Meta:
        model = Task
        fields = ['id', 'title', 'finished_date', 'board_list']        


class UserDashboardSerializer(serializers.ModelSerializer):
    completed_task = CompletedTaskSerializer(
        many= True, 
        source= 'get_completed_task', 
        read_only = True,
    )

    class Meta:
        model = User
        fields = ['username', 'completed_task']  

    def get_completed_task(self, instance):
        completed_task_count = instance.get_completed_task().count()
        return completed_task_count

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["completed_task_count"] = self.get_completed_task(instance)
        return representation
