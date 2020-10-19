from django.contrib import admin
from django.urls import path, include
from gold_app.views import *
from django.contrib.auth.views import LogoutView

app_name = 'gold_app'


urlpatterns = [
    # path('register', register),
    # path('', user_login, name= "home"),
    # path('conapp', user_login, name='conapp'),
    # path('add-data', addData),
    # path('trans-data',transData),
    path('show/', show),
    # path('logout',logout_view , name = "logout"),
    # path('logout', logout_view, name='logout'),

]
