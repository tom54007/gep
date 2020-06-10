from django.urls import path, re_path
from . import views


app_name = 'basework'

urlpatterns = [
    path('annual_data/uploadexcel', views.importExcel),
]