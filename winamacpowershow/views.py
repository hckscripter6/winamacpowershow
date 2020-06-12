from django.shortcuts import render
from info.models import Update

def index(request):
    update = Update.objects.order_by('-id').all()
    return render(request, 'winamacpowershow/index.html', {'update': update})