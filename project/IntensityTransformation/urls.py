"""IntensityTransformation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^app/$',views.app),
    url(r'^uploadImage/$',views.upload_file,name="uploadImage"),
    url(r'^operation/$',views.operations, name="operations"),
    url(r'^negative/$',views.negative, name="negative"),
    url(r'^power-gamma/$', views.power, name="power-gamma"),
    url(r'^hist-matching/$', views.matching, name="hist-matching"),
    url(r'^hist-equalisation/$', views.equilisation, name="hist-equalisation"),
    url(r'^histogram/$', views.histogram, name="histogram"),
]
