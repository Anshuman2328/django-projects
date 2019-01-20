from django.conf.urls import url
from.import views   # this is a new line that was added to import views.


urlpatterns = [
    url(r'^$', views.index),
    url(r'^field$', views.field),
    url(r'^clear$', views.clear),

    
    # url(r'^user_list$^', views.user_list)


]
