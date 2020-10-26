from . import views
from django.urls import path, include
from gold_app.views import User


app_name = 'gold_app'


urlpatterns = [
    path('show/', views.show),
    path('add/',views.add),
    path('home/', views.home_view),
    path('display',views.display),
]
