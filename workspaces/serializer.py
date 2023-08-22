from rest_framework import serializers
from .models import Workspace, WorkspacesMembership

class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = '__all__'  


class WorkspacesMembershipSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(source='member.username', read_only=True)
    email = serializers.CharField(source='member.email', read_only=True)
    
    
    class Meta:
        model = WorkspacesMembership
        fields = ['id',  'username',
                  'email',  'access_level']

class WorkspaceWithMembersSerializer(serializers.ModelSerializer):
    members = serializers.StringRelatedField(many=True)  
    boards = serializers.SerializerMethodField()

    class Meta:
        model = Workspace
        fields = '__all__'

    def get_boards(self, obj):
        return [board.name for board in obj.get_boards()]
    
class WorkspacesMembershipDetailSerializer(serializers.ModelSerializer):
    workspace = WorkspaceSerializer()
    member = serializers.StringRelatedField()

    class Meta:
        model = WorkspacesMembership
        fields = '__all__'
