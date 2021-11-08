from django.urls import path
from . import views

urlpatterns = [
  path('', views.list, name="projects_list"),
  path('find-project/<str:pk>/', views.index, name="projects_index"),
  path('new-project/', views.create, name="projects_create")
]