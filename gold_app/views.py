from .forms import GLAForm 
from gold_app.models import User
from django.shortcuts import render, HttpResponse
from django.contrib.postgres.search import SearchVector

def home_view(request): 
    context ={} 
    form = GLAForm(request.POST or None, request.FILES or None) 
    if form.is_valid(): 
        form.save() 
    context['form']= form 
    return render(request, "home.html", context) 


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
        seens = User.objects.filter(user_branch__icontains=request.GET.get('q')).values()    
        print(seens)
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
