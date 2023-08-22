from rest_framework import serializers
from .models import Workspace, WorkspacesMembership
from users.models import User
from users.serializers import UserSerializer


class WorkspaceSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    members = serializers.SerializerMethodField(many=True)
    boards = serializers.SerializerMethodField()

    def get_members(self, obj):
        queryset = WorkspacesMembership.objects.filter(workspace=obj)
        return WorkspacesMembershipSerializer(queryset, many=True, context={"request": self.context['request']}).data


    def get_boards(self, obj):
        return [board.name for board in obj.get_boards()]
    

    class Meta:
        model = Workspace
        fields = [
            'id',
            'owner',
            'title',
            'description',
            'members'
        ]
        read_only_fields = ['owner']
 


class WorkspacesMembershipSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(source='member.username', read_only=True)
    email = serializers.CharField(source='member.email', read_only=True)
    

    
    class Meta:
        model = WorkspacesMembership
        fields = ['id',  'username',
                  'email',  'access_level']


class WorkspaceshortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = ['id', 'title']
