from django.db import models
# from django.contrib.auth.models import UserManager
# Create your models here.


LEAD_STATUSS = (
        ('cancelled', 'Cancelled'),
        ('disbursement done', 'Disbursement Done'),
        ('lead', 'Lead'),
        ('request submitted', 'Request Submitted'),
        ('retrieval completed', 'Retrieval Completed'),
    )
STATUS_GLA_REQUEST = (('cancelled','Cancelled'),
            ('verified','Verified'),
            ('request_taken','Request Taken'),
            ('submitted','Submitted'),
    )
STATUS_RETRIEVAL_LOAN = (('sanctioned','Sanctioned'),
            ('required','Required'),
    )

STATUS_RETRIEVAL = (('required','Required'),
            ('completed','Completed'),
    )
#pending (paid but not received gold from customer )

STATUS_DISBURSEMENT = (('disbursed','Disbursed'),
            ('ready for scheduling','Ready for Scheduling'),
    )

#cancelled from customer after retrieval bcz customer is not agree terms( T&C ) 

REQ_RETRIEVAL = (('yes','Yes'),
            ('no','No'),
) 

REQ_TENURE = (('12','12'),('24','24'),('36','36'),)

class branch(models.Model):
    branch_code = models.CharField(primary_key=True, max_length = 100)
    branch_name = models.CharField(unique = True,default  = 'HO', max_length = 30,blank = True, null=True)
    # s_no = models.AutoField()
    # def __unicode__(self):
    #     return u'%s' % (self.branch_name)
    # class Meta:
    #     ordering = []


class collection_day (models.Model):
    collection_day = models.CharField(max_length = 100,blank = True, null=True )
    coll_id = models.IntegerField(primary_key = True,default = 1)

class collection_time(models.Model):
    coll_time_id = models.IntegerField(primary_key = True,default = 1)
    collection_time = models.CharField( max_length=50,blank = True, null=True)

class community(models.Model):
    community_name = models.CharField(max_length = 100,blank = True, null=True)
    comm_branch = models.ForeignKey(branch, on_delete=models.CASCADE,null = True)

class center(models.Model):
    center_code = models.CharField(primary_key = True, max_length = 100)
    center_name = models.CharField(max_length= 100,blank = True, null=True)
    center_branch =  models.ForeignKey(branch,on_delete=models.CASCADE)
    collection_day = models.ForeignKey(collection_day,to_field = 'coll_id',null = True,on_delete=models.CASCADE)
    collection_start_time = models.ForeignKey(collection_time,to_field = 'coll_time_id',null = True,on_delete=models.CASCADE)
    # fo = models.ForeignKey(fo)
    # coll_review_day = models.ForeignKey(collection_day,on_delete=models.CASCADE)
    # coll_review_time = models.ForeignKey(collection_time,on_delete=models.CASCADE)
    # center_status = MultiSelectField(max_length = 12, choices = CHOISES) #multiple choise
    # vcm_status = MultiSelectField(max_length = 12, choices = status_vcm )



class group (models.Model):
    group_code = models.CharField(primary_key = True, max_length = 100)
    group_name = models.CharField(max_length = 100,blank = True, null=True)
    # group_leader = models.ForeignKey(member, on_delete=models.CASCADE)
    # group_center_code = models.ForeignKey(center,on_delete=models.CASCADE)
    collection_time = models.ForeignKey(collection_time,on_delete=models.CASCADE)
class Role(models.Model):
    role_name = models.CharField(max_length = 100, null = True)

class User(models.Model):
    role = models.ManyToManyField(Role,null = True)
    mem_num = models.CharField(primary_key = True, default = '00000',max_length = 100)
    first_name = models.CharField(max_length = 100, blank = True, null=True)
    middle_name = models.CharField(max_length = 100, blank = True, null=True)
    last_name = models.CharField(max_length = 100, blank = True, null=True)
    aadhar = models.CharField(max_length = 100, blank = True, null=True)
    pan = models.CharField(max_length = 100, blank = True, null=True)
    date_of_birth = models.DateField( blank = True, null=True)
    # marital_status = models.MultiSelectField()
    mobile_registred = models.CharField(max_length = 100, blank = True, null=True)
    mobile_whatsapp = models.CharField(max_length = 100, blank = True, null=True)
    date_of_signup = models.DateField(blank = True, null=True)
    date_of_memstart = models.DateField( blank = True, null=True)
    # collection_frequency = models.MultiSelectField()
    cot_balance = models.IntegerField( blank = True, null=True)
    cot_emi = models.IntegerField( blank = True, null=True)
    sa_balance = models.IntegerField( blank = True, null=True)
    user_group = models.ForeignKey(group,to_field= 'group_code', null = True,on_delete=models.CASCADE)
    # fo = models.ForeignKey(fo,)
    user_branch = models.ForeignKey(branch,to_field = 'branch_code', on_delete = models.CASCADE, null = True)
    user_center = models.ForeignKey(center,to_field = 'center_code', on_delete =  models.CASCADE, null = True)
    # user_status  = models.MultiSelectField()
    # user_role = 
    # community = 
    date_of_food_distribution = models.DateField( null = True)

    # objects = UserManager()

class GL_lead(models.Model):
    #foreign_key in GLA
    member = models.ForeignKey(User,to_field = 'mem_num',default = 'mem_num', on_delete=models.CASCADE)
    lead_branch =  models.ForeignKey(branch, to_field = 'branch_name',default = 'HO', on_delete=models.CASCADE)
    lead_id = models.AutoField(primary_key = True)
    lead_status = models.CharField(max_length=20,choices=LEAD_STATUSS,default = 'null', blank = True,null=True)
    # lead_status = models.CharField(max_length = 40)Multiselect field
    date_of_lead = models.DateField(default = '')
    status_gla_request = models.CharField(max_length=20,choices=STATUS_GLA_REQUEST,default = 'null',blank = True,null=True)
    # gla_status = models.Char Multi Select
    # status_gla = multiple choice
    # status_gla_request = multiple choice
    status_retrieval_loan = models.CharField(max_length=20,choices=STATUS_RETRIEVAL_LOAN,default = 'null',blank = True,null=True)
    #status_retrieval_loan = multiple choice
    status_retrieval = models.CharField(max_length=20,choices=STATUS_RETRIEVAL,default = 'null',blank = True,null=True)
    # staus_retrieval = multiple_choice
    status_disbursement = models.CharField(max_length=20,choices=STATUS_DISBURSEMENT,default = 'null', blank = True,null=True)
    # status_disbursement = multiple choice 



class GLA(models.Model):
    gla_gl = models.ForeignKey(GL_lead, to_field = 'lead_id',default = 1, on_delete=models.CASCADE)
    gla_branch = models.ForeignKey(branch, to_field = 'branch_name', on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, to_field = 'mem_num', default = '0000', on_delete=models.CASCADE)
    gla_application_id = models.IntegerField( primary_key = True, default = 1)
    cot_balance = models.DecimalField(max_digits=9, decimal_places=2)
    dummy = models.CharField(max_length = 30,default = 'hello')
    retrieval = models.CharField(max_length=20,choices=REQ_RETRIEVAL,default = 'null',blank = True, null=True)
    param_interest_rate_gl = models.IntegerField(blank = True,default = 1, null=True)
    param_interest_rate_glp = models.IntegerField(blank = True,default = 1, null=True)
    param_interest_rate_glg = models.IntegerField(blank = True,default = 1, null=True)
    param_lpf_rate = models.IntegerField(blank = True,default = 1, null=True)
    param_share_purchase_rate = models.IntegerField(blank = True,default = 1, null=True)
    param_base_share_value = models.IntegerField(blank = True,default = 1, null=True)
    param_gold_appraisal_rate = models.IntegerField(blank = True,default = 1, null=True)
    param_gold_rate_gl = models.IntegerField(blank = True,default = 1, null=True)
    param_gold_rate_glp = models.IntegerField(blank = True, default = 1,null=True)
    param_gold_rate_glg = models.IntegerField(blank = True,default = 1, null=True)
    param_cot_repay_rate_recommended = models.IntegerField(default = 1,blank = True, null=True)
    req_gold_loan_amount = models.IntegerField(default = 1,blank = True, null=True)
    req_netweight_gold = models.BooleanField(blank = True, null=True)
    req_max_loan_amount_gl = models.IntegerField(default = 1,blank = True, null=True)
    req_max_loan_amount_glp = models.IntegerField(default = 1,blank = True, null=True)
    req_max_loan_amount_glg = models.IntegerField(default = 1,blank = True, null=True)
    calc_emi_1_year_gl = models.IntegerField(default = 1,blank = True, null=True)
    calc_emi_2_year_gl = models.IntegerField(default = 1,blank = True, null=True)
    calc_emi_3_year_gl = models.IntegerField(default = 1,blank = True, null=True)
    # req_retrieval_required = models.CharField(max_length=20,choices=STATUS_DISBURSEMENT,default = 'null', blank = True,null=True)
    req_tenure = models.CharField(max_length=20,choices=REQ_TENURE,default = 'null',blank = True, null=True)
    # req_vriddhi_gla = models.FileField(upload_to='documents/')
    # status_gla = multiple choice
    # status_gla_request = multiple choice
    #status_retrieval_loan = multiple choice
    # staus_retrieval = multiple_choice
    #status_disbursement = multiple_choice
    #gla_submit_request = multiple_choice
    tr_lead_entered = models.DateField(default = '2020-12-02',blank = True, null=True)
    tr_request_taken = models.DateField(blank = True, null=True,default = '2020-12-02')
    tr_gla_cancelled = models.DateField(blank = True, null=True,default = '2020-12-02')
    retrieval_loan_amount_requested = models.IntegerField(blank = True, null=True)
    tr_retrieval_loan_requested = models.DateField(blank = True, null=True,default = '2020-12-02')
    tr_retrieval_completed = models.DateField(blank = True, null=True,default = '2020-12-02')
    reason_for_cancellation = models.TextField(default = 'Cancel',blank = True, null=True)
    disbursement_schedule = models.DateField(blank = True, null=True,default = '2020-12-02')
    tr_disbursement = models.DateField(blank = True, null=True,default = '2020-12-02')
    gl_gold_net_weight = models.IntegerField(default = 1,blank = True, null=True)
    gl_loan_amount = models.IntegerField(default = 1,blank = True, null=True)
    gl_tenure = models.IntegerField(default = 1,blank = True, null=True)
    # gl_loan_type = multiple choice 
    gl_interest_rate = models.IntegerField(default = 1,blank = True, null=True)
    # gl_membership_fee = multiple choice
    # gl_mode_of_payment = multiple choice
    gl_date_of_first_installment = models.DateField(default = '2020-12-02',blank = True, null=True)
    gl_lpf = models.IntegerField(default = 1,blank = True, null=True)
    gl_share_purchase = models.IntegerField(default = 1,blank = True, null=True)
    gl_gold_appraisal_fee = models.IntegerField(default = 1,blank = True, null=True)
    gl_cot_repayment = models.IntegerField(default = 1,blank = True, null=True)
    gl_cot_repayment = models.IntegerField(default = 1,blank = True, null=True)
    gl_total_retrieval_amount = models.IntegerField(default = 1,blank = True, null=True)

class gold_lot(models.Model):
    # member = models.ForeignKey(member,on_delete = models.CASCADE)
    gla = models.ForeignKey(GLA,on_delete = models.CASCADE)
    gross_weight = models.DecimalField(max_digits=9, decimal_places=2,blank = True, null=True)#
    net_weight = models.DecimalField(max_digits=9, decimal_places=2,blank = True, null=True)#
    outstanding_amount = models.IntegerField(blank = True, null=True)#
    jewller_last_interest_paid_when = models.DateField(null = True,blank = True)#
    jewller_name = models.CharField(max_length = 50,blank = True, null=True)#
    jewller_mobile = models.CharField(max_length=12,blank = True, null=True)#
    jewller_address = models.CharField( max_length=128,blank = True, null=True)#
    jewller_landmark = models.CharField(max_length = 30,blank = True, null=True)
    jewller_working_hours = models.CharField(max_length = 30,blank = True, null=True)#
    jewller_holidays = models.CharField(max_length = 30,blank = True, null=True)#
    # status_gold_lot = multiple choice
    # status_retrieval = multiple choice
    schedule_retrieval = models.DateField(blank = True, null=True)
    # retrieval_transporter = models.ForeignKey(transporter,on_delete=models.CASCADE)
    tr_created = models.DateField(blank = True, null=True)
    tr_gold_lot_received = models.DateField(blank = True, null=True)
    tr_handover_to_admin = models.DateField(blank = True, null=True)
    tr_cancellation = models.DateField(blank = True, null=True)
    # retrieval_outcome = multiple choice 


# class GL_lead(models.Model):

#     member = models.ForeignKey(User,to_field = 'mem_num', on_delete=models.CASCADE, null = True)
#     lead_branch =  models.ForeignKey(branch, to_field = 'branch_name', on_delete=models.CASCADE, null = True)
#     lead_status = models.CharField(max_length = 40, null = True)
#     date_of_lead = models.DateField(null = True)
#     # status_gla_request = Multiselect field



