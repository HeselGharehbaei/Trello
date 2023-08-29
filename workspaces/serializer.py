from rest_framework import serializers
from .models import Workspace, WorkspacesMembership
from users.models import User
from users.serializers import UserWorkspacesSerializer,UserBriefSerializer



class WorkspacesMembershipSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(source='member.username', read_only=True)
    email = serializers.CharField(source='member.email', read_only=True)
    

    
    class Meta:
        model = WorkspacesMembership
        fields = ['id',  'username',
                  'email',  'access_level','members']

class WorkspaceSerializer(serializers.ModelSerializer):
   
    members = serializers.SerializerMethodField()
    boards = serializers.SerializerMethodField()
    owner = UserBriefSerializer(read_only=True, default=serializers.CurrentUserDefault()) 
    def get_members(self, obj):
        queryset = WorkspacesMembership.objects.filter(workspace=obj)
        return WorkspacesMembershipSerializer(queryset, many=True, context={"request": self.context['request']}).data


    def get_boards(self, obj):
        return [board.name for board in obj.get_boards()]
    
    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user  # تنظیم owner با اطلاعات کاربر جاری
        return super().create(validated_data)
    
    class Meta:
        model = Workspace
        fields = [
           'id',
            'owner',
            'title',
            'description',
            'members'
        ]
        #fields ='__all__'
        read_only_fields = ['owner']
 





class WorkspaceshortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = ['title',"id"]
