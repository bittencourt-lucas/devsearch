from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="projects_list"),
    path('find-project/<str:pk>/', views.index, name="projects_index"),
    path('new-project/', views.create, name="projects_create"),
    path('update-project/<str:pk>', views.update, name="projects_update"),
    path('delete-project/<str:pk>', views.delete, name="projects_delete")
]