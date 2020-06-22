import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
django.setup()
from work import tasks
from basework import admin, utils, models


# tasks.do_calc('江苏省', 2021)


# 查地区数据
areadata = models.Annual_data.objects.filter(year='2017')
utils.read_items_name
utils.read_prov_items_name

for i in areadata:
    print(i.r_d)
