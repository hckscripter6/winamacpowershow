from django import forms
from django.contrib.auth.models import User
from info.models import Info

class EditInfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['name', 'content']