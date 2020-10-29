from .forms import GLAForm,Gl_leadForm
from gold_app.models import User,GLA,GL_lead
from django.shortcuts import render, HttpResponse
from django.contrib.postgres.search import SearchVector

def lead_view(request):
    form = Gl_leadForm()
    if request.method == "POST":
        form = Gl_leadForm(request.POST)
        if form.is_valid(): 
            try:
                form.save()
                return redirect('/lead')
            except:
                pass
    else:
        form = Gl_leadForm() 

    return render(request, "lead.html", locals()) 


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
