from rest_framework import serializers
from django.contrib.auth.models import User
from . models import project , Task , Comment

class project_serializers(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        slug_field = "username",
        queryset = User.objects.all()
    )
    class Meta:
        model = project 
        fields = '__all__'

class task_serializers(serializers.ModelSerializer):
    project = serializers.SlugRelatedField(
        slug_field='name',
        queryset=project.objects.all()
    )
    assigned_to = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )
    class Meta:
        model = Task 
        fields = '__all__'


class comment_serializers(serializers.ModelSerializer):
    task = serializers.SlugRelatedField(
        slug_field='title',
        queryset=Task.objects.all()
    )
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )
    class Meta:
        model = Comment
        fields = '__all__'