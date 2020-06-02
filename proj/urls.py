"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from django.views.static import serve
from ckeditor_uploader import views as ckeditor_uploader_views
from django.views.decorators.cache import never_cache
from django.conf import settings


urlpatterns = [
    path('', include('work.urls'), name='work'),
    path('admin/', admin.site.urls),

    path('ckeditor/upload/', ckeditor_uploader_views.upload, name='ckeditor_upload'),
    path('ckeditor/browse/', never_cache(ckeditor_uploader_views.browse), name='ckeditor_browse'),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),

]


if True:
    from django.conf.urls import url
    from django.views.static import serve

    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
        url(r'^static/(?P<path>.*)$', serve,  {'document_root': settings.STATIC_ROOT}, name='static'),

    ]
