from django.urls import path, include
from rest_framework.routers import DefaultRouter

from example import views


router = DefaultRouter()
router.register('users', views.UserProfileViewSet, basename="user_profile")


urlpatterns = [
    path('user/edit/', views.UserEditView.as_view(), name="user_edit"),
    path('user/<int:pk>/json/', views.UserProfileJsonView.as_view(), name="user_json"),
    path('', include(router.urls)),
]
