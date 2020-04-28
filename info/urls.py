from django.urls import path
from . import views

urlpatterns = [
    path('summer-show/', views.SummerShow, name="summer-show"),
    path('toy-show/', views.ToyShow, name="toy-show"),
    path('scholarship/', views.Scholarship, name="scholarship"),
    path('golf-cart-policy/', views.GolfCart, name="golf-cart"),
    path('exhibitor-information/', views.ExhibitorInfo, name="exhibitor-info"),
    path('exhibitor-camping/', views.ExhibitorCamping, name="exhibitor-camping"),
    path('toy-vendor/', views.ToyVendor, name="toy-vendor"),
    path('food-vendor/', views.FoodVendor, name="food-vendor"),
    path('flea-market-vendor/', views.FleaMarket, name="flea-market"),
    path('directions/', views.Directions, name="directions"),
    path('contact/', views.Contact, name="contact"),
    path('club-members/', views.ClubInfo, name="club-info"),
]