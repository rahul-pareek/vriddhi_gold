from . import views
from django.urls import path, include
from gold_app.views import User


app_name = 'gold_app'


urlpatterns = [

    path('show/', views.show,name = 'show'),
    path('add/',views.add,name = 'add'),
    path('home/', views.home_view,name = 'home'),
    path('gla_update/',views.gla_update,name = 'gla_update'),
    path('display',views.display,name = 'display'),
    path('lead',views.lead_view,name = 'lead'),
    path('main/',views.main_view,name = 'main'),
    path('',views.main_view,name = 'main_page'),
    path('gl',views.gl_lead_view,name = 'gl'),
    path('delete_gla/<int:gla_gl>',views.delete_GLA,name = 'delete_gla'),
    path('update_gla/<int:gla_gl>',views.update_GLA,name ='update_gla' ),
    path('update/',views.update_GLA,name = 'update'),
    path('submit_gla/<int:gla_gl>',views.submit_GLA,name = 'submit'),
    path('gold_lot',views.gold_lot_view,name ='gold_lot'),
    # path('update/<int:gla_id>',views.update),

]
