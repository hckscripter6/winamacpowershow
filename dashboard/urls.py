from django.urls import path
from . import views

urlpatterns = [
    path('info/edit/<int:id>/', views.editInfo, name="edit-page"), 
    path('update/edit/<int:id>/', views.editUpdate, name="edit-update-page"),
    path('update/create/', views.createUpdate, name="create-update-page"),
    path('update/<int:id>/delete/', views.deleteUpdate, name="delete-update"),
    path('', views.dashboard, name="dashboard"),
]

