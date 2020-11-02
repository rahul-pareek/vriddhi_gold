from gold_app.models import User,GLA,GL_lead, branch
from .forms import GLAForm,Gl_leadForm
from django.shortcuts import render, HttpResponse
from django.contrib.postgres.search import SearchVector

def main_view(request):

    return render(request, "main_page.html")

def lead_view(request):

    Gl_lead_Form = Gl_leadForm(request.POST)
    user_branch_id = request.GET.get('user_branch_id')
    mem_num = request.GET.get('mem_num')

    if request.method == "POST":

        Gl_lead_Form = Gl_leadForm(request.POST)
        print("I am in")

        if Gl_lead_Form.is_valid():

                lead_branch = branch.objects.get(branch_code=user_branch_id)
                member = User.objects.get(mem_num=mem_num)
                print("Hello", Gl_lead_Form.cleaned_data.get('lead_status'))
                Gl_lead_instance = GL_lead.objects.create(member = member, lead_branch = lead_branch, lead_status = Gl_lead_Form.cleaned_data.get('lead_status'), date_of_lead = Gl_lead_Form.cleaned_data.get('date_of_lead'))
                print(Gl_lead_instance.lead_branch)
                Gl_lead_instance.save()
                return render(request, "lead.html", {'Gl_lead_Form': Gl_lead_Form, 'mem_num': mem_num, 'user_branch_id': user_branch_id})

        else:

            print("Invalid")
            Gl_lead_Form = Gl_leadForm(request.POST)

    return render(request, "lead.html", {'Gl_lead_Form': Gl_lead_Form, 'mem_num': mem_num, 'user_branch_id': user_branch_id})


def edit(request, id):

    gl_lead = GL_lead.objects.get(id=id)  
    return render(request,'', {'gl_lead':gl_lead}) 


def update(request, id):

    gl_lead = GL_lead.objects.get(id=id)  
    form = Gl_leadForm(request.POST, instance = gl_lead)  
    if form.is_valid():  
        form.save()  
        return redirect("")  


def destroy(request, id):

    gl_lead = GL_lead.objects.get(id=id)  
    gl_lead.delete()  
    return redirect("")  


def home_view(request):

    context ={} 
    user_branch_id = request.GET.get('user_branch_id')
    mem_num = request.GET.get('mem_num')
    # print(user_branch_id,mem_num,'--------Hello sir!!!!!----------')
    # user_detail = {'user_branch_id':user_branch_id,'mem_num':mem_num}
    form = GLAForm()
    if request.method == "POST":
        form = GLAForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/home')
            except:
                pass
    else:
        form = GLAForm() 
    return render(request, "home.html", locals()) 


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
        # print(seens)
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
    # gla =GLA.objects.all()[:10]
    # dis = {
    #     "cot_balance":transactions
    # }
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
