from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index$', views.index),
    url(r'^login$', views.login_page),
    url(r'^register$', views.register_page),
    url(r'^users/register$', views.register),
    url(r'^users/login$', views.login),
    # url(r'^dashboard/admin$', views.dashboard),
    url(r'^dashboard$', views.dashboard),
    url(r'^users/new$', views.users_new),
    url(r'^users/show/(?P<id>\d+)$', views.users_homepage),
    url(r'^users/edit/(?P<id>\d+)$', views.edit),
    url(r'^users/edit_users', views.edit_users),
    url(r'^users/delete/(?P<id>\d+)$', views.delete),
    url(r'^logout', views.logout),
]