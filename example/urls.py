from django.urls import path, include
from rest_framework.routers import DefaultRouter

from example import views


router = DefaultRouter()
router.register('users', views.UserProfileViewSet, basename="user_profile")


urlpatterns = [
    path('user/edit/', views.UserEditView.as_view(), name="user_edit"),
    path('', include(router.urls)),
]
