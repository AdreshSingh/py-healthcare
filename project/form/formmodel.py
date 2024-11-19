
from django import forms
from .models import FormModel
class MyFormModel(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = ['name','age','file']