from django import forms
from app_module.models import Module

class ModuleForm(forms.ModelForm):

    class Meta:
        model = Module
        fields = ['project', 'name', 'describe']