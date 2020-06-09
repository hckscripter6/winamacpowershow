from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EditInfoForm
from info.models import Info

# Create your views here.
def editPage(request, id):
    page = Info.objects.get(id=id)
    if request.method == 'POST':
        form = EditInfoForm(request.POST, instance=page)
        
        if form.is_valid():
            form.save()
            
    else:
        form = EditInfoForm(instance=page)
        
    return render(request, 'dashboard/info-edit.html', { 'form': form })
        