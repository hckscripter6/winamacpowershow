from django.shortcuts import render
from .models import Info

# Create your views here.
def SummerShow(request):
    info = Info.objects.get(name="Summer Show Info")
    return render(request, 'info/summer_show.html', {'info': info})
    