from django.db import models
from multiselectfield import MultiSelectField
# from phonenumber_field.modelfields import PhoneNumberField
#  phone = PhoneNumberField(null=False, blank=False, unique=True)
CHOISES = (('active','ACTIVE'),
('inactive','INACTIVE'),
('under review','UNDER REVIEW'))

status_vcm = (('active','ACTIVE'),
('probation','PROBATION'))

# GLA_req_retrieval_required =(('yes','YES'),
# ('no','NO'))

# GLA_req_tenure = (('12','12'),
# ('24','24'),
# ('36','36'))



# Create your models here.
class branch(models.Model):
    branch_name = models.CharField(max_length = 30)
    branch_code = models.CharField(max_length = 3)
    # s_no = models.AutoField()
    # def __unicode__(self):
    #     return u'%s' % (self.branch_name)

class collection_day (models.Model):
    collection_day = models.CharField(max_length = 30)

class collection_time(models.Model):
    collection_time = models.DateTimeField()

class community(models.Model):
    community_name = models.CharField(max_length = 30)
    comm_branch = models.ForeignKey('branch',to_field = 'branch_code', on_delete=models.CASCADE)

class center(models.Model):
    center_num = models.CharField(max_length = 30)
    center_name = models.CharField(max_length= 30)
    center_branch =  models.ForeignKey(branch,to_field = 'branch_code',on_delete=models.CASCADE)
    collection_day = models.ForeignKey(collection_day,on_delete=models.CASCADE)
    collection_start_time = models.ForeignKey(collection_time,on_delete=models.CASCADE)
    # fo = models.ForeignKey(fo)
    # coll_review_day = models.ForeignKey(collection_day,on_delete=models.CASCADE)
    # coll_review_time = models.ForeignKey(collection_time,on_delete=models.CASCADE)
    center_status = MultiSelectField(max_length = 12, choices = CHOISES) #multiple choise
    vcm_status = MultiSelectField(max_length = 12, choices = status_vcm )

class group (models.Model):
    group_num = models.CharField(max_length = 30)
    group_name = models.CharField(max_length = 30)
    # group_leader = models.ForeignKey(member, on_delete=models.CASCADE)
    center = models.ForeignKey(center,on_delete=models.CASCADE)
    collection_time = models.ForeignKey(collection_time,on_delete=models.CASCADE)

class GLA(models.Model):
    branch = models.ForeignKey(branch , on_delete=models.CASCADE)
    # borrower = models.ForeignKey(member , on_delete=models.CASCADE)
    cot_balance = models.DecimalField(max_digits=9, decimal_places=2)
    param_interest_rate_gl = models.IntegerField()
    param_interest_rate_glp = models.IntegerField()
    param_interest_rate_glg = models.IntegerField()
    param_lpf_rate = models.IntegerField()
    param_share_purchase_rate = models.IntegerField()
    param_base_share_value = models.IntegerField()
    param_gold_appraisal_rate = models.IntegerField()
    param_gold_rate_gl = models.IntegerField()
    param_gold_rate_glp = models.IntegerField()
    param_gold_rate_glg = models.IntegerField()
    param_cot_repay_rate_recommended = models.IntegerField()
    req_gold_loan_amount = models.IntegerField()
    req_netweight_gold = models.BooleanField()
    # req_retrieval_required = #multiple choice
    # req_tenure = multiple choices
    # req_vriddhi_gla = models.FileField(upload_to='documents/')
    # status_gla = multiple choice
    # status_gla_request = multiple choice
    #status_retrieval_loan = multiple choice
    # staus_retrieval = multiple_choice
    #status_disbursement = multiple_choice
    #gla_submit_request = multiple_choice
    tr_lead_entered = models.DateField()
    tr_request_taken = models.DateField()
    tr_gla_cancelled = models.DateField()
    retrieval_loan_amount_requested = models.IntegerField()
    tr_retrieval_loan_requested = models.DateField()
    tr_retrieval_completed = models.DateField()
    reason_for_cancellation = models.TextField()
    disbursement_schedule = models.DateField()
    tr_disbursement = models.DateField()
    gl_gold_net_weight = models.IntegerField()
    gl_loan_amount = models.IntegerField()
    gl_tenure = models.IntegerField()
    # gl_loan_type = multiple choice 
    gl_interest_rate = models.IntegerField()
    # gl_membership_fee = multiple choice
    # gl_mode_of_payment = multiple choice
    gl_date_of_first_installment = models.DateField()
    gl_lpf = models.IntegerField()
    gl_share_purchase = models.IntegerField()
    gl_gold_appraisal_fee = models.IntegerField()
    gl_cot_repayment = models.IntegerField()
    gl_cot_repayment = models.IntegerField()
    gl_total_retrieval_amount = models.IntegerField()

class gold_lot(models.Model):
    # member = models.ForeignKey(member,on_delete = models.CASCADE)
    gla = models.ForeignKey(GLA,on_delete = models.CASCADE)
    gross_weight = models.DecimalField(max_digits=9, decimal_places=2)
    net_weight = models.DecimalField(max_digits=9, decimal_places=2)
    outstanding_amount = models.IntegerField()
    jewller_name = models.CharField(max_length = 50)
    jewller_mobile = models.CharField(max_length=12)
    jewller_address = models.CharField( max_length=128)
    jewller_landmark = models.CharField(max_length = 30)
    jewller_working_hours = models.CharField(max_length = 30)
    jewller_holidays = models.CharField(max_length = 30)
    # status_gold_lot = multiple choice
    # status_retrieval = multiple choice
    schedule_retrieval = models.DateField()
    # retrieval_transporter = models.ForeignKey(transporter,on_delete=models.CASCADE)
    tr_created = models.DateField()
    tr_gold_lot_received = models.DateField()
    tr_handover_to_admin = models.DateField()
    tr_cancellation = models.DateField()
    # retrieval_outcome = multiple choice 

class Role(models.Model):
    role_name = models.CharField(max_length = 30)

class User(models.Model):
    role = models.ManyToManyField(Role)
    mem_num = models.CharField(max_length = 30)
    first_name = models.CharField(max_length = 30)
    middle_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    aadhar = models.CharField(max_length = 30)
    pan = models.CharField(max_length = 30)
    date_of_birth = models.DateField()
    # marital_status = models.MultiSelectField()
    mobile_registred = models.CharField(max_length = 10)
    mobile_whatsapp = models.CharField(max_length = 10)
    date_of_signup = models.DateField()
    date_of_memstart = models.DateField()
    # collection_frequency = models.MultiSelectField()
    cot_balance = models.IntegerField()
    cot_emi = models.IntegerField()
    sa_balance = models.IntegerField()
    group = models.ForeignKey(group,on_delete=models.CASCADE)
    # fo = models.ForeignKey(fo,)
    branch = models.ForeignKey(branch,on_delete = models.CASCADE)
    center = models.ForeignKey(center,on_delete =  models.CASCADE)
    # user_status  = models.MultiSelectField()
    # user_role = 
    # community = 
    date_of_food_distribution = models.DateField()


   


    # User_roles = (
    #     ('fo', 'FO'),
    #     ('transporter', 'Transporter'),
    #     ('scm', 'SCM'),
    #     ('Am','AM'),
    #     ('Rm','RM')
    #     ('admin gold','Admin Gold'),
    # )
    # roles = models.CharField(max_length=20,choices=THEME_CHOICES, unique=True)

    # def __str__(self):
    #     return self.roles
    # # staff = 
    

# class User_role(models.Model):
#     user = models.ManyToManyField(User)
#     role = models.ManyToManyField(Role)





