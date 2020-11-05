from django import forms 
from .models import GLA,GL_lead

class GLAForm(forms.ModelForm):
    # def __init__(self,*args, **kwargs):
        # super(GLAForm, self).__init__(*args, **kwargs)
        # user_detail = kwargs.pop('user_detail')
        # self.fields['user_branch_id'].label = 'user_branch'
        # print(user_detail['user_branch_id'], user_detail['mem_num'],'Hello')
        # self.dummy = user_detail['user_branch_id']
            # self.fields['mem_num'].label = user_detail['mem_num']

        

    class Meta:

        model = GLA 
        fields = "__all__"

class Gl_leadForm(forms.ModelForm):

    class Meta:

        model = GL_lead
        fields = ('lead_status', 'date_of_lead','status_gla_request','status_retrieval_loan','status_retrieval','status_disbursement')
        exclude = ('member', 'lead_branch')

      #  widgets = {
      #      'date_of_lead':
      #      forms.DateInput(attrs={'class':'datepicker'}),
      #  }