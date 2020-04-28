from django.shortcuts import render
from .models import Info

# Create your views here.
def SummerShow(request):
    info = Info.objects.get(name="Summer Show Info")
    events = Info.objects.get(name="Summer Show Page Event Schedule")
    return render(request, 'info/summer_show.html', {'info': info, 'events': events})

def ToyShow(request):
    return render(request, 'info/toy_show.html')

def Scholarship(request):
    info = Info.objects.get(name="Northern Indiana Power from the Past Scholarships")
    return render(request, 'info/scholarship.html', {'info': info})
    
def GolfCart(request):
    info = Info.objects.get(name="Golf Cart Policy")
    return render(request, 'info/golf_cart.html', {'info': info})

def ExhibitorInfo(request):
    info = Info.objects.get(name="Exhibitor Information")
    return render(request, 'info/exhibitor_info.html', {'info': info})

def ExhibitorCamping(request):
    info = Info.objects.get(name="Camping for Exhibitors")
    return render(request, 'info/exhibitor_camping.html', {'info': info})

def ToyVendor(request):
    info = Info.objects.get(name="Toy Vendor Info")
    return render(request, 'info/toy_vendor.html', {'info': info})

def FoodVendor(request):
    info = Info.objects.get(name="Food Vendor Information")
    return render(request, 'info/food_vendor.html', {'info': info})

def FleaMarket(request):
    info = Info.objects.get(name="Flea Market Vendor Info")
    return render(request, 'info/flea_market.html', {'info': info})

def Directions(request):
    return render(request, 'info/directions.html')

def Contact(request):
    info = Info.objects.get(name="Contact Information")
    return render(request, 'info/contact.html', {'info': info})

def ClubInfo(request):
    members = Info.objects.get(name="Club Members")
    dates = Info.objects.get(name="Club Meeting Dates")
    return render(request, 'info/club_info.html', {'members': members, 'dates': dates})


