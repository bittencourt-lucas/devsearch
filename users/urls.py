from django.urls import path

from . import views

urlpatterns = [
    path('', views.profiles, name="profiles_list"),
    path('profile/<str:pk>/', views.user_profile, name="user_profile"),
]