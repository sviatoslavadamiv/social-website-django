from django.urls import include, path
from . import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path("edit/", views.edit, name="edit"),
    path('users/', views.user_list, name='user_list'),
    path('users/<username>/', views.user_detail, name='user_detail'),
]
