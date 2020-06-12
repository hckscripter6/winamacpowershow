from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import InfoForm, UpdateForm
from info.models import Info, Update

# Create your views here.
def dashboard(request):
    info = Info.objects.all()
    update = Update.objects.order_by('-id').all()
    return render(request, 'dashboard/dashboard.html', {'info': info, 'update': update})
    
    
def editInfo(request, id):
    page = Info.objects.get(id=id)
    if request.method == 'POST':
        form = InfoForm(request.POST, instance=page)
        if form.is_valid():
            form.save() 
    else:
        form = InfoForm(instance=page)
    return render(request, 'dashboard/info-edit.html', { 'form': form })



def createUpdate(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UpdateForm()
    return render(request, 'dashboard/info-edit.html', {'form': form})

def deleteUpdate(request, id):
    update = Update.objects.get(id=id).delete()
    
        
        
def editUpdate(request, id):
    update = Update.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=update)
        if form.is_valid():
            form.save()  
    else:
        form = UpdateForm(instance=update)
    return render(request, 'dashboard/info-edit.html', {'form': form})


        