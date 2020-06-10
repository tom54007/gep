from django.urls import path, re_path
from . import views


app_name = 'basework'

urlpatterns = [
    path('importexcel', views.importExcel, name='importExcel'),
]