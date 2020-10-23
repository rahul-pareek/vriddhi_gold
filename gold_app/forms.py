from django import forms 
from .models import GLA
class GLAForm(forms.ModelForm):
    class Meta: 
        model = GLA 
        fields = "__all__"