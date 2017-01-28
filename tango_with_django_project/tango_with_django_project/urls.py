from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rango/', include('rango.urls')),
    url(r'^admin/', admin.site.urls),
]
