from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^set_name$', views.set_name, name='set_name'),
    url(r'^', views.index, name='index')

]