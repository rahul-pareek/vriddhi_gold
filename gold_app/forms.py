from django import forms 
from .models import GLA

class GLAForm(forms.ModelForm):
    # def __init__(self,*args, **kwargs):
    #     self.user_branch_id = kwargs.pop('user_branch_id')
    #     self.fields['user_branch_id'].label = user_branch_id
    #     super(GLAForm, self).__init__(*args, **kwargs)
        

    class Meta: 
        model = GLA 
        fields = "__all__"