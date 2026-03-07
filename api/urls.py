from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_user.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('projects', views.project_view.as_view({'get': 'list', 'post': 'create'}), name='projects'),
    path('task/',views.task_view.as_view({'get':'list','post':'create'})),  
    path('comment/',views.comment_view.as_view({'get':'list','post':'create'}))
]