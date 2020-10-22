from gold_app.models import User
from django.shortcuts import render, HttpResponse
from django.contrib.postgres.search import SearchVector

def show(request):
    usr = User.objects.all()[:10]
    # import pdb
    # pdb.set_trace()
    
    stu = {
    "mem_num": usr
     }
    return render(request, './show_member.html', stu)

def add(request):
    search_vector = SearchVector('user_group_id','user_branch_id')
    if ('q' in request.GET) and request.GET.get('q').strip():
        query_string=request.GET.get('q')
        seens = User.objects.annotate(search = search_vector).filter(search=query_string)
        print(q)
    else:
        seens=None
    return render(request,'show_member.html',{'seens':seens})
