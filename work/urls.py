from django.urls import path, re_path
from . import views


app_name = 'work'

urlpatterns = [
#     path('', views.index, name='index'),
    re_path(r'^province/(?P<province_name>\w+)/(?P<year>\d{4})$', views.province_year_simple,
            name='province_year_simple'),
    re_path(r'^prov/(?P<province_name>\w+)/(?P<year>\d{4})$', views.province_year_all,
            name='province_year_all'),
    re_path(r'^city/(?P<province_name>\w+)/(?P<city_name>\w+)/(?P<year>\d{4})$', views.city_year_data,
            name='city_year_data'),
    re_path(r'^process/(?P<province_name>\w+)/(?P<year>\d{4})$', views.process, name='process'),
    path('article/<int:article_id>', views.article_json, name='article_json'),
    ]