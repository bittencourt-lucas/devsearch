from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('', views.profiles, name="profiles_list"),
    path('profile/<str:pk>/', views.user_profile, name="user_profile"),
    path('account/', views.user_account, name="account"),
    path('edit-account/', views.edit_account, name="edit_account"),
]