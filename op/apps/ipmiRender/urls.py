from django.urls import path, include
from . import views

app_name = 'ipmiRender'
urlpatterns = [
    path('index/', views.index, name="index"),
    path('get/', views.get_rrs, name="get"),
    path('op/',views.op,name="op")
]
