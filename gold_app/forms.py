from django import forms 
from .models import GLA

class GLAForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        user_detail = kwargs.pop('user_detail')
        
        super(GLAForm, self).__init__(*args, **kwargs)
        print(user_detail['user_branch_id'], user_detail['mem_num'],'Hello')
        if user_detail :
            self.dummy = user_detail['user_branch_id']
            # self.fields['mem_num'].label = user_detail['mem_num']

        # 

    class Meta: 
        model = GLA 
        fields = "__all__"