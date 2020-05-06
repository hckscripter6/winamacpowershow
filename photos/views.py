from django.shortcuts import render
from .models import Image, Set
# Create your views here.
def Photos(request):
    set = Set.objects.order_by('-id').all()
    return render(request, 'photos/photos.html', {'set': set})