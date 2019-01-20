from django.conf.urls import url
from.import views   # this is a new line that was added to import views.

urlpatterns = [
    url(r'^$', views.index),
    url(r'^hello$', views.hello),
    url(r'^new$', views.new),  # the word "views" next to "r" is something that user will see
    url(r'^create$', views.create),
    url(r'^(?P<val>\d+)$', views.number),  # to give a variable in regex, put it inside the <> and ? means start of the regex, \d means a nu is coming through.
    url(r'^(?P<val>\d+)/edit$', views.edit),
    url(r'^(?P<val>\d+)/delete$', views.delete),



    # path('', views.index, name='index'), this is another way to do this, you can leave the path blank in between quotations and define the name or root or '/' as index

    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),  in this we give name detail and this will get added to home/root or '/' 

    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),

    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]






# ###########%%%%%%%%%%%%%%%%%%%   Views.py file below ######################%%%%%%%%%%%%%%%%%%%%





from django.shortcuts import render, HttpResponse, redirect


def index(request):   # This is a function just like before this will handle whatever is sent to it. The name index can be anything but it needs to updated in the urls.py
    response = "Helloo I have requested you as my first request"
    return HttpResponse(response)

def hello(request):
    response = "Placeholder to later display all the list of blogs.  This is just a test"
    return HttpResponse(response)

def new(request):
    response = "Placeholder to later display new blogs.  This is just a test"
    return HttpResponse(response)

def create(request):
    response = "Helloo I have requested you as my first request"
    return redirect('/')

def number(request, val):
    response = "This is a new blog"
    return HttpResponse(response + val)

def edit(request, val):
    response = " You are now editing blog no"
    return HttpResponse(response + val)


# these three examples below are the ones that could also be used to show the user the path


# def detail(request, your_id):
#     return HttpResponse("You're now looking at your id and that is  %s." % your_id)

# def results(request, number):
#     response = "You're have requested a new number and it is  %s."
#     return HttpResponse(response % number)

# def vote(request, variablenumber):
#     return HttpResponse("Your variable no is  %s." % variablenumber)
# *************** the lines 32 to 40 shows another way of doing these

# @@@@@@@@@@@@@@@@@@ the method below shows shows we can use f strings and send the HttpResponse directly@@@@@@@

# def edit(request, val):
#     return HttpResponse(f'you are now viewing the no {val}')

def delete(request, val):
    response = "Helloo I have requested you as my first request"
    return redirect('/')




# Create your views here.
