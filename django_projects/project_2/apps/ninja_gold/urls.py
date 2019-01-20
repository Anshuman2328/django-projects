from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^reset$', views.reset),
]


















































# from django.conf.urls import url
# from.import views   # this is a new line that was added to import views.


# urlpatterns = [
#     url(r'^$', views.index),
#     url(r'^process$', views.process),
#     url(r'^clear$', views.clear),

    
#     # url(r'^user_list$^', views.user_list)


# ]

