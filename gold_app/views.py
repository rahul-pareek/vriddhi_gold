from .forms import GLAForm 
from gold_app.models import User
from django.shortcuts import render, HttpResponse
from django.contrib.postgres.search import SearchVector

def home_view(request): 
    context ={} 
    # user_branch_id = request.GET.get('user_branch_id')
    # mem_num = request.GET.get('mem_num')
    form = GLAForm() 
    if request.method == "POST":
        form = GLAForm(request.POST)
        if form.is_valid(): 
            form.save() 
    
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

# def add(request):
#     # search_vector = SearchVector('user_branch_id')
#     if ('q' in request.GET) and request.GET.get('q').strip():
#     #     query_string=request.GET.get('q')
#         seens = User.objects.filter(user_branch_id__id__icontains=request.GET.get('q')).value()
#         print(seens)
#     else:
#         seens=None
#     return render(request,'show_member.html',{'seens':seens})
