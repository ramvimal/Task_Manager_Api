from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from . serializer import project_serializers , task_serializers , comment_serializers
from . models import project , Task , Comment
from rest_framework.permissions import BasePermission

# Create your views here.

class register_user(APIView):
    def post(self,request):
        username = request.data.get("username")
        password = request.data.get("password")

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=400)

        User.objects.create_user(username=username, password=password)

        return Response({"message": "User created"})

class IsProjectOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class project_view(viewsets.ModelViewSet):
    serializer_class = project_serializers
    permission_classes = [IsAuthenticated,IsProjectOwner]

    def get_queryset(self):
        return project.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class IsTaskOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.project.owner == request.user

class task_view(viewsets.ModelViewSet):
    serializer_class = task_serializers
    permission_classes = [IsAuthenticated,IsTaskOwner]
    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'project']


class comment_view(viewsets.ModelViewSet):
    serializer_class = comment_serializers
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()