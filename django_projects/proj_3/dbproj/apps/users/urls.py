from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.main, name='homepage'),
    url(r'^users/createuser$', views.createuser, name='displayuser'),
    url(r'^users/display$', views.index),
    url(r'^users/showuser/(?P<id>\d+)$', views.showuser),
    url(r'^users/edituser/(?P<id>\d+)$', views.edituser),
    url(r'^users/updateuser/(?P<id>\d+)$', views.updateuser),
    url(r'^users/deleteuser/(?P<id>\d+)$', views.deleteuser),
    # url(r'^users/(?P<id>\d+)/update$', views.update),


]
