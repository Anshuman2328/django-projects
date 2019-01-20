from django.conf.urls import url
from.import views   # this is a new line that was added to import views.

urlpatterns = [
    # url(r'^$', views.index),
    url(r'^$', views.index),
    url(r'^field$', views.field),
    url(r'^list$', views.list_of_users), # this is where url gets redirected to and then it checks in views and particular file to execute, in this case list_of_users
    url(r'^back$', views.back),


    

    
]
    # url(r'^list$', views.list_of_users), # this is where url gets redirected to and then it checks in views and particular file to execute, in this case list_of_users
    # url(r'^hello$', views.hello),
    # url(r'^new$', views.new),  # the word "views" next to "r" is something that user will see
    # url(r'^create$', views.create),
    # url(r'^(?P<val>\d+)$', views.number),  # to give a variable in regex, put it inside the <> and ? means start of the regex, \d means a nu is coming through.
    # url(r'^(?P<val>\d+)/edit$', views.edit),
    # url(r'^(?P<val>\d+)/delete$', views.delete),
    # path('', views.index, name='index'), this is another way to do this, you can leave the path blank in between quotations and define the name or root or '/' as index
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),  in this we give name detail and this will get added to home/root or '/' 
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
