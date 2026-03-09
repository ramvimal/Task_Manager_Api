from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path , include

router = DefaultRouter()

router.register('projects',views.project_view,basename="project")
router.register('task',views.task_view)
router.register('comment',views.comment_view)

urlpatterns = [
    path('register', views.register_user.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls