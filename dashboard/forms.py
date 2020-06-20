from django import forms
from django.contrib.auth.models import User
from info.models import Info, Update
from photos.models import Image

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['name', 'content']
        
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Update
        fields = ['name', 'content', 'created_at']
        
class PhotosForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['photo', 'set']