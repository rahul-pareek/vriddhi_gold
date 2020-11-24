from gold_app.models import User,GLA,GL_lead, branch,gold_lot
from .forms import GLAForm,Gl_leadForm,Gold_lotForm
from django.db.models import Count
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.postgres.search import SearchVector
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)

def home_view(request):
    user_branch_id = request.GET.get('user_branch_id')
    mem_num = request.GET.get('mem_num')
    # print(user_branch_id,mem_num,'--------Hello sir!!!!!----------')
    # user_detail = {'user_branch_id':user_branch_id,'mem_num':mem_num}
    form = GLAForm()
    if request.method == "POST":
        form = GLAForm(request.POST)
        if form.is_valid():
            try:
                # gla_application_id = form.cleaned_data['gla_application_id']
                # cot_balance = form.cleaned_data['cot_balance']
                # dummy = form.cleaned_data['dummy']
                # retrieval = form.cleaned_data['retrieval']
                # param_interest_rate_gl = form.cleaned_data['param_interest_rate_gl']
                # param_interest_rate_glp = form.cleaned_data['param_interest_rate_glp']
                # param_interest_rate_glg = form.cleaned_data['param_interest_rate_glg']
                # param_lpf_rate = form.cleaned_data['param_lpf_rate']
                # param_share_purchase_rate = form.cleaned_data['param_share_purchase_rate']
                # param_base_share_value = form.cleaned_data['param_base_share_value']
                # param_gold_appraisal_rate = form.cleaned_data['param_gold_appraisal_rate']
                # param_gold_rate_gl = form.cleaned_data['param_gold_rate_gl']
                # param_gold_rate_glp = form.cleaned_data['param_gold_rate_glp']
                # param_gold_rate_glg = form.cleaned_data['param_gold_rate_glg']
                # param_cot_repay_rate_recommended = form.cleaned_data['param_cot_repay_rate_recommended']
                # req_gold_loan_amount = form.cleaned_data['req_gold_loan_amount']
                # req_netweight_gold = form.cleaned_data['req_netweight_gold']
                # req_max_loan_amount_gl = form.cleaned_data['req_max_loan_amount_gl']
                # req_max_loan_amount_glp = form.cleaned_data['req_max_loan_amount_glp']
                # req_max_loan_amount_glg = form.cleaned_data['req_max_loan_amount_glg']
                # req_tenure = form.cleaned_data['req_tenure']
                # tr_lead_entered = form.cleaned_data['tr_lead_entered']
                # tr_request_taken = form.cleaned_data['tr_request_taken']
                # tr_gla_cancelled = form.cleaned_data['tr_gla_cancelled']
                # retrieval_loan_amount_requested = form.cleaned_data['retrieval_loan_amount_requested']
                # tr_retrieval_loan_requested = form.cleaned_data['tr_retrieval_loan_requested']
                # tr_retrieval_completed = form.cleaned_data['tr_retrieval_completed']
                # reason_for_cancellation = form.cleaned_data['reason_for_cancellation']
                # disbursement_schedule = form.cleaned_data['disbursement_schedule']
                # tr_disbursement = form.cleaned_data['tr_disbursement']
                # gl_gold_net_weight = form.cleaned_data['gl_gold_net_weight']
                # gl_loan_amount = form.cleaned_data['gl_loan_amount']
                # gl_tenure = form.cleaned_data['gl_tenure']
                # gl_interest_rate = form.cleaned_data['gl_interest_rate']
                # gl_date_of_first_installment = form.cleaned_data['gl_date_of_first_installment']
                # gl_lpf = form.cleaned_data['gl_lpf']
                # gl_share_purchase = form.cleaned_data['gl_share_purchase']
                # gl_gold_appraisal_fee = form.cleaned_data['gl_gold_appraisal_fee']
                # gl_cot_repayment = form.cleaned_data['gl_cot_repayment']
                # gl_cot_repayment = form.cleaned_data['gl_cot_repayment']
                # gl_total_retrieval_amount = form.cleaned_data['gl_total_retrieval_amount']
                # g = GLA.objects.create(gla_application_id=gla_application_id,cot_balance=cot_balance,dummy=dummy,retrieval=retrieval,param_interest_rate_gl=param_interest_rate_gl,
                #         param_interest_rate_glp=param_interest_rate_glp,param_interest_rate_glg=param_interest_rate_glg,param_lpf_rate=param_lpf_rate,
                #         param_share_purchase_rate=param_share_purchase_rate,param_base_share_value=param_base_share_value,param_gold_appraisal_rate=param_gold_appraisal_rate,
                #         param_gold_rate_gl=param_gold_rate_gl,param_gold_rate_glp=param_gold_rate_glp,param_gold_rate_glg=param_gold_rate_glg,
                #         param_cot_repay_rate_recommended=param_cot_repay_rate_recommended,req_gold_loan_amount=req_gold_loan_amount,req_netweight_gold=req_netweight_gold,
                #         req_max_loan_amount_gl=req_max_loan_amount_gl,req_max_loan_amount_glp=req_max_loan_amount_glp,req_max_loan_amount_glg=req_max_loan_amount_glg,
                #         req_tenure=req_tenure,tr_lead_entered=tr_lead_entered,tr_request_taken=tr_request_taken,tr_gla_cancelled=tr_gla_cancelled,retrieval_loan_amount_requested=retrieval_loan_amount_requested,
                #         tr_retrieval_loan_requested=tr_retrieval_loan_requested,tr_retrieval_completed=tr_retrieval_completed,reason_for_cancellation=reason_for_cancellation,
                #         disbursement_schedule=disbursement_schedule,tr_disbursement=tr_disbursement,gl_gold_net_weight=gl_gold_net_weight,gl_loan_amount=gl_loan_amount,
                #         gl_tenure=gl_tenure,gl_interest_rate=gl_interest_rate,gl_date_of_first_installment=gl_date_of_first_installment,gl_lpf=gl_lpf,
                #         gl_share_purchase=gl_share_purchase,gl_gold_appraisal_fee=gl_gold_appraisal_fee,gl_cot_repayment=gl_cot_repayment, gl_total_retrieval_amount= gl_total_retrieval_amount,messages_received = 0)
                # g.save()
                print('--------!---------')
                form.save()
                return redirect('/home')
            except:
                pass
    else:
        print('this is invalid form')
        form = GLAForm() 
    return render(request, "home.html", locals())


def gold_lot_view(request):
    form = Gold_lotForm()
    if request.method == "POST":
        form = Gold_lotForm(request.POST)
        if form.is_valid():
            try:
                
                return redirect('/gold_lot')
            except:
                pass 
    else:
        form = Gold_lotForm() 
    return render(request, "./gold_lot.html", locals())

def update_GLA(request,gla_gl):
    # gla_gl = request.GET.get('gla_gl')
    # gla_branch = request.GET.get('gla_branch')
    # borrower = request.GET.get('borrower')
    instance = GLA.objects.get(gla_gl=gla_gl) 
    if request.method == "POST":
        print("Enter")
        form = GLAForm(request.POST)
        if form.is_valid():
            Gl_lead_form_details = GLA.objects.create(borrower = mem_num, gla_branch=user_branch_id, gla_gl = lead_id, gla_application_id = form.cleaned_data.get('gla_application_id'),
                                                            cot_balance = form.cleaned_data.get('cot_balance'), param_interest_rate_gl = form.cleaned_data.get('param_interest_rate_gl'),param_interest_rate_glp= form.cleaned_data.get('param_interest_rate_glp'),
                                                            param_interest_rate_glg = form.cleaned_data.get('param_interest_rate_glg'), param_lpf_rate = form.cleaned_data.get('param_lpf_rate'), param_share_purchase_rate = form.cleaned_data.get('param_share_purchase_rate'),
                                                            param_base_share_value = form.cleaned_data.get('param_base_share_value'), param_gold_rate_gl = form.cleaned_data.get('param_gold_rate_gl'), param_gold_rate_glp = form.cleaned_data.get('param_gold_rate_glp'),
                                                            param_cot_repay_rate_recommended = form.cleaned_data.get('param_cot_repay_rate_recommended'), req_gold_loan_amount = form.cleaned_data.get('req_gold_loan_amount'), req_netweight_gold = form.cleaned_data.get('req_netweight_gold'),
                                                            tr_lead_entered = form.cleaned_data.get('tr_lead_entered'), tr_request_taken = form.cleaned_data.get('tr_request_taken'), tr_gla_cancelled = form.cleaned_data.get('tr_gla_cancelled'),
                                                            retrieval_loan_amount_requested = form.cleaned_data.get('retrieval_loan_amount_requested'), tr_retrieval_loan_requested = form.cleaned_data.get('tr_retrieval_loan_requested'), tr_retrieval_completed = form.cleaned_data.get('tr_retrieval_completed'),
                                                            reason_for_cancellation = form.cleaned_data.get('reason_for_cancellation'), disbursement_schedule = form.cleaned_data.get('disbursement_schedule'), tr_disbursement = form.cleaned_data.get('tr_disbursement'),
                                                            gl_gold_net_weight = form.cleaned_data.get('gl_gold_net_weight'), gl_loan_amount = form.cleaned_data.get('gl_loan_amount'), gl_tenure = form.cleaned_data.get('gl_tenure'),
                                                            gl_interest_rate = form.cleaned_data.get('gl_interest_rate'), gl_date_of_first_installment = form.cleaned_data.get('gl_date_of_first_installment'), gl_lpf = form.cleaned_data.get('gl_lpf'),
                                                            gl_share_purchase = form.cleaned_data.get('gl_share_purchase'), gl_gold_appraisal_fee = form.cleaned_data.get('gl_gold_appraisal_fee'), gl_cot_repayment = form.cleaned_data.get('gl_cot_repayment'),
                                                            gl_total_retrieval_amount = form.cleaned_data.get('gl_total_retrieval_amount')
                                                            )
            Gl_lead_form_details.save()
            print("valid")
            return render(request,"/main_page")
        else:
            print("Invalid")
            GLAForm = GLAForm(request.POST)
            print(Gl_lead_form_details)
    # instance = GLA.objects.get(id=gla_application_id)
    # form = GLAForm(request.POST,instance)
    # if request.method == 'POST':
    #     form = GLAForm(request.POST,instance = instance)
    #     if form.is_valid():
    #         form_data = form.cleaned_data
    #         form_submit = 1
    #     if form_submit == 1:
    #         form.save()
    # else:
    #     form = GLAForm(instance)
    # form = GLAForm()
    # if request.method == "POST":
    #     form = GLAForm(request.POST)
    #     if form.is_valid():
    #         try:
    #             form.save()
    #             return redirect('/update_gla')
    #         except:
    #             pass
    # else:
    #     form = GLAForm() 
    return render(request, "update_gla.html", locals()) 

def submit_GLA(request,gla_gl):
    instance = GLA.objects.get(gla_gl=gla_gl)
    return render(request,'submit_gla.html',{'instance':instance})

def delete_GLA(request, gla_gl):
    instance = GLA.objects.get(gla_gl = gla_gl)
    instance.delete()
    return redirect('/gold_lot_id')

    # Gold_loat_Form = Gold_lotForm(request.POST)
    # if request.method == "POST":
    #     Gold_loat_Form = Gold_lotForm(request.POST)
    #     if Gold_loat_Form.is_valid():
    #             return render(request, "./gold_lot.html")
    #     else:
    #         print("Invalid")
    #         Gold_loat_Form = Gold_lotForm(request.POST)
    # return render(request, "./gold_lot.html")

def main_view(request):
    return render(request, "main_page.html")

def gl_lead_view(request):
    gl = GL_lead.objects.all()
    print(gl)
    # mem_num = request..GET.get('mem_num')
    # user_branch_id = request.GET.get('user_branch_id') 
    
    # print(gla)
    return render(request, './views.html', locals())

def lead_view(request):

    Gl_lead_Form = Gl_leadForm(request.POST)
    user_branch_id = request.GET.get('user_branch_id')
    mem_num = request.GET.get('mem_num')

    if request.method == "POST":

        Gl_lead_Form = Gl_leadForm(request.POST)
        # print("I am in")

        if Gl_lead_Form.is_valid():

                lead_branch = branch.objects.get(branch_code=user_branch_id)
                member = User.objects.get(mem_num=mem_num)
                # print("Hello", Gl_lead_Form.cleaned_data.get('lead_status'))
                Gl_lead_instance = GL_lead.objects.create(member = member, lead_branch = lead_branch, lead_status = Gl_lead_Form.cleaned_data.get('lead_status'), date_of_lead = Gl_lead_Form.cleaned_data.get('date_of_lead'))
                # print(Gl_lead_instance.lead_branch)
                Gl_lead_instance.save()
                return render(request, "lead.html", {'Gl_lead_Form': Gl_lead_Form, 'mem_num': mem_num, 'user_branch_id': user_branch_id})

        else:

            print("Invalid")
            Gl_lead_Form = Gl_leadForm(request.POST)

    return render(request, "lead.html", {'Gl_lead_Form': Gl_lead_Form, 'mem_num': mem_num, 'user_branch_id': user_branch_id})


# def edit(request, gla_id):
#     gl_lead = GL_lead.objects.get(id=gla_id)  
#     return render(request,'', {'gl_lead':gl_lead}) 


# def update(request, gla_id):
    
#     gl_lead = GL_lead.objects.get(id=gla_id)  
#     member = request.GET.get('member')
#     # gl_lead = get_object_or_404(Gl_leadForm, id = id)
#     if gl_lead:
#         gl_lead.member = member
#         gl_lead.save()
#     # context["form"] = form  
#     return render(request,"update_view.html",{'gl_lead':gl_lead})  


# def destroy(request, id):
#     gl_lead = GL_lead.objects.get(id=id)  
#     gl_lead.delete()  
#     return redirect("")  

def gla_update(request):
    gl = GLA.objects.all()
    # print(gla)
    return render(request,'./update.html', locals())
 
def show(request):
    usr = User.objects.all()[:10]
    # import pdb
    # pdb.set_trace()
    stu = {
    "mem_num": usr
     }
    return render(request, './show_member.html', stu)

def add(request):
    search_vector = SearchVector('user_branch_id')
    if ('q' in request.GET) and request.GET.get('q').strip():
        query_string=request.GET.get('q')
        seens = User.objects.filter(user_branch__branch_name__icontains=request.GET.get('q')).values()
        # seens = User.objects.group_by('mem_num','date_of_memstart')

        print(seens)
        # import  pdb; pdb.set_trace()
    else:
       seens=None
    return render(request,'./show_member.html',{'seens': seens})

def display(request):
    transactions = []
    if ('q' in request.GET) and request.GET.get('q').strip():
        transactions = GLA.objects.filter(gla_application_id=request.GET.get('q'))
        print(transactions)
    else:
        transactions = None
    return render(request,'./display.html',{'transactions':transactions})


# def add(request):
#     # search_vector = SearchVector('user_branch_id')
#     if ('q' in request.GET) and request.GET.get('q').strip():
#     #     query_string=request.GET.get('q')
#         seens = User.objects.filter(user_branch_id__id__icontains=request.GET.get('q')).value()
#         print(seens)
#     else:
#         seens=None
#     return render(request,'show_member.html',{'seens':seens})
