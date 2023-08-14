from rest_framework import serializers
from .models import Workspace, WorkspacesMembership

class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = '__all__'  


class WorkspacesMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkspacesMembership
        fields = '__all__'  

