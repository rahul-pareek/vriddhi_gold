from django.shortcuts import render
from gold_app.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
# Create your views here.
def show(request):
    print('.............')
    usr = User.objects.order_by('mem_num')
    print(usr,'................')
    # usr = []
    # if request.GET.get('q'):
    #     # print ("----------")
    #     # print (request.GET)
    #     print ("----------")
    #     try:
    #         usr = User.objects.filter(mem_num=request.GET.get('q'))[0:100]
    #         usr = member[0]
    #     except:
    #         usr = None
        
    #     print(usr)
    #     print(request.GET.get('q'))
    #     # user = User.objects.filter(mem_num__icontains=request.GET.get('q'))

    return HttpResponse('hello!!!!')
