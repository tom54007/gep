from django.urls import path, re_path
from . import views


app_name = 'work'

urlpatterns = [
    path('annual_data/uploadexcel', views.importExcel),
]