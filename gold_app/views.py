from gold_app.models import User,GLA,GL_lead, branch,gold_lot
from .forms import GLAForm,Gl_leadForm,Gold_lotForm
from django.db.models import Count
from django.shortcuts import render, HttpResponse
from django.contrib.postgres.search import SearchVector
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)

def gold_lot_view(request):
    
    Gold_loat_Form = Gold_lotForm(request.POST)
    if request.method == "POST":

        Gold_loat_Form = Gold_lotForm(request.POST)
        # print("I am in")

        if Gold_loat_Form.is_valid():
                # gold_load_instance = GL_lead.objects.create(gla_gl = gla_gl, gla_branch = gla_branch,borrower=borrower, lead_status = Gl_lead_Form.cleaned_data.get('lead_status'), date_of_lead = Gl_lead_Form.cleaned_data.get('date_of_lead'))
                gold_load_instance.save()
                return render(request, "update.html")

        else:

            print("Invalid")
            Gold_loat_Form = Gold_lotForm(request.POST)

    return render(request, "update.html")

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


def edit(request, id):
    context = {}
    gl_lead = GL_lead.objects.get(id=id)  
    return render(request,'', {'gl_lead':gl_lead}) 


def update(request, gla_id):
    
    gl_lead = GL_lead.objects.get(id=gla_id)  
    member = request.GET.get('member')
    # gl_lead = get_object_or_404(Gl_leadForm, id = id)
    if gl_lead:
        gl_lead.member = member
        gl_lead.save()
    # context["form"] = form  
    return render(request,"update_view.html",{'gl_lead':gl_lead})  


def destroy(request, id):

    gl_lead = GL_lead.objects.get(id=id)  
    gl_lead.delete()  
    return redirect("")  

def gla_update(request):
    gl = GLA.objects.all()
    # print(gla)
    return render(request,'./update.html', locals())

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
