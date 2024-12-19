from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter
from django.urls import path
from users.views import UserCreateAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

router = DefaultRouter()

urlpatterns = [
    #path("users/", UsersListAPIView.as_view(), name="users-list"),
    path("registration/", UserCreateAPIView.as_view(), name="habit-create"),  # Регистрация пользователя
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]#+router.urls
