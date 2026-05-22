from django.urls import path

from .views import (
    register_user,
    CustomTokenObtainPairView,
)

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", register_user),

    path("login/", CustomTokenObtainPairView.as_view()),

    path("refresh/", TokenRefreshView.as_view()),
]