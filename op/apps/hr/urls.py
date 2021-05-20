from django.urls import path, include
from . import views

app_name = 'hr'
urlpatterns = [
    path('index/', views.index, name="index"),
    path('get/', views.get_rrs, name="get"),
]
