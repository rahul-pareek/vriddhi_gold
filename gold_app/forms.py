from django import forms 
from .models import GLA,GL_lead,gold_lot

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
        fields = ('gla_gl','gla_branch','borrower','gla_application_id','cot_balance','dummy','retrieval','param_interest_rate_gl','param_interest_rate_glp','param_interest_rate_glg','param_lpf_rate','param_share_purchase_rate','param_base_share_value','param_gold_appraisal_rate','param_gold_rate_gl','param_gold_rate_glp','param_gold_rate_glg','param_cot_repay_rate_recommended','req_gold_loan_amount','req_netweight_gold','req_max_loan_amount_gl','req_max_loan_amount_glp','req_max_loan_amount_glg','req_tenure','tr_lead_entered','tr_request_taken','tr_gla_cancelled','retrieval_loan_amount_requested','tr_retrieval_loan_requested','tr_retrieval_completed','reason_for_cancellation','disbursement_schedule','tr_disbursement','gl_gold_net_weight','gl_loan_amount','gl_tenure','gl_interest_rate','gl_date_of_first_installment','gl_lpf','gl_share_purchase','gl_gold_appraisal_fee','gl_cot_repayment','gl_cot_repayment','gl_total_retrieval_amount')
        exclude = ('calc_emi_1_year_gl','calc_emi_2_year_gl','calc_emi_3_year_gl')

class Gold_lotForm(forms.ModelForm):
    class Meta:
        
        model  = gold_lot
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