from django.urls import path
from . import views

urlpatterns = [
    path('edit/<int:id>/', views.editPage, name="edit-page"),    
]