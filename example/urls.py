from django.urls import path

from example import views


urlpatterns = [
    path('user/edit/', views.UserEditView.as_view(), name="user_edit"),
]
