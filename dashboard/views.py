from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import InfoForm, UpdateForm, PhotosForm
from info.models import Info, Update
from photos.models import Image

# Create your views here.

@login_required
def dashboard(request):
    info = Info.objects.all()
    update = Update.objects.order_by('-id').all()
    return render(request, 'dashboard/dashboard.html', {'info': info, 'update': update})
    
@login_required
def editInfo(request, id):
    page = Info.objects.get(id=id)
    if request.method == 'POST':
        form = InfoForm(request.POST, instance=page)
        if form.is_valid():
            form.save() 
    else:
        form = InfoForm(instance=page)
    return render(request, 'dashboard/info-edit.html', { 'form': form })


@login_required
def createUpdate(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UpdateForm()
    return render(request, 'dashboard/info-edit.html', {'form': form})

@login_required
def deleteUpdate(request, id):
    update = Update.objects.get(id=id).delete()
    return redirect('dashboard')
    
        
@login_required
def editUpdate(request, id):
    update = Update.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=update)
        if form.is_valid():
            form.save()  
    else:
        form = UpdateForm(instance=update)
    return render(request, 'dashboard/info-edit.html', {'form': form})

@login_required
def photoUpload(request):
    if request.method == 'POST':
        form = PhotosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PhotosForm()
    return render(request, 'dashboard/photos.html', {'form': form})


        