import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
django.setup()
from work import tasks


tasks.do_calc('江苏省', 2021)

