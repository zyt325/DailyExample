from django.urls import path, include
from . import views

app_name = 'note'
urlpatterns = [
    path('index/', views.index, name="index"),
    path('get/', views.get_rrs, name="get"),
    path('add-note/',views.add_note,name="add-note"),
    path('edit-note/',views.edit_note,name="edit-note"),
    path('op/',views.op,name="op"),
    path('upload-img/',views.uploadImg,name="upload-img"),
]
