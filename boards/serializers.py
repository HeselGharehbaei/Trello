from rest_framework import serializers
from .models import Board
from .models import List
from .models import Task
from .models import Comment
from .models import Label

class BoradSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class LableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fiels = '__all__'
        