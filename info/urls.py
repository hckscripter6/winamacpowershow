from django.urls import path
from . import views

urlpatterns = [
    path('summer-show/', views.SummerShow, name="summer-show")
]