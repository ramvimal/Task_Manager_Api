from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from . serializer import project_serializers , task_serializers , comment_serializers
from . models import project , Task , Comment
# Create your views here.

class register_user(APIView):
    def post(self,request):
        user = User.objects.create_user(
            username = request.data["username"],
            password = request.data["password"]
        )
        return Response({"Message":"User Created"})


class project_view(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = project_serializers
    queryset = project.objects.all()

class task_view(viewsets.ModelViewSet):
    serializer_class = task_serializers
    queryset = Task.objects.all()

class comment_view(viewsets.ModelViewSet):
    serializer_class = comment_serializers
    queryset = Comment.objects.all()