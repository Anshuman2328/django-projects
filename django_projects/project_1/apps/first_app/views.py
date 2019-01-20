from django.shortcuts import render, HttpResponse, redirect
from time import gmtime,strftime
from django.utils.crypto import get_random_string


def index(request):
    return render(request, "first_app/index.html")


# def generate(request):
#     # unique_id = get_random_string(length=32)
#     if 'counter' not in request.session:
#         request.session['counter'] = 0
#     # request.session['random'] = unique_id
#     request.session['counter'] +=1
    # return render(request, "first_app/index.html")
def field(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter'] +=1
    if request.method == "POST":
        print(request.POST["namekey"])
        request.session["fname"] = request.POST["namekey"]  # this is how we can get key value pair from request.POST "in the from" and save it to request.session["any name variable"]
        request.session["lname"] = request.POST["last_name"]
        request.session["description"] = request.POST["desc"]
        return redirect('/list')   # this url "/list" tells where to go. This is in urls.py 
    elif request.method == "GET":
        return render(request, "first_app/index.html")

def list_of_users(request):
    # request.session["name"] 
    # # "blog_name" = request.form(['desc'])
    return render(request, "first_app/list_of_users.html")

def back(request):
    request.session.clear()
    return redirect("/")










# $%$%$%$%$%$%$%$%$%$ below is the exmple of the usage of time function $%$%$%$%$%$%$%$%$%$%$%$

# def index(request):
#     time = {
#         "current_time_display" : strftime("%Y-%m-%d %H:%M %p", gmtime())
#     }
#     return render(request, "first_app/index.html", time)
# $%$%$%$%$%$%$%$%$%$ above is the exmple of the usage of time function $%$%$%$%$%$%$%$%$%$%$%$


# $%$%$%$%$%$%$%$%$%$ below 2 were exmples of the usage of sessions $%$%$%$%$%$%$%$%$%$%$%$
# def index(request):
#     if request.method == "POST":
#         # print(request.POST["name"])
#         request.session["name"] = request.POST["namekey"]  # this is how we can get key value pair from request.POST "in the from" and save it to request.session["any name variable"]
#         request.session["description"] = request.POST["desc"]
#         return redirect('/list')   # this url "/list" tells where to go. This is in urls.py 
#     elif request.method == "GET":
#         return render(request, "first_app/index.html")

# def list_of_users(request):
#     # request.session["name"] 
#     # # "blog_name" = request.form(['desc'])
#     return render(request, "first_app/list_of_users.html")
# $%$%$%$%$%$%$%$%$%$ above 2 were exmples of the usage of sessions $%$%$%$%$%$%$%$%$%$%$%$


# def index(request):
#     context = {
#         "emailtohtml" : "ash@gmail.com",
#         "first_name2html"  : "ash",
#         "last_name2html" : "purohit"
#     }
#     return render(request, "first_app/index.html", context)


















#  This is the first assignment <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,  start assignment 1


# def index(request):   # This is a function just like before this will handle whatever is sent to it. The name index can be anything but it needs to updated in the urls.py
#     response = "Helloo I have requested you as my first request"
#     return HttpResponse(response)

# def hello(request):
#     response = "Placeholder to later display all the list of blogs.  This is just a test"
#     return HttpResponse(response)

# def new(request):
#     response = "Placeholder to later display new blogs.  This is just a test"
#     return HttpResponse(response)

# def create(request):
#     response = "Helloo I have requested you as my first request"
#     return redirect('/')

# def number(request, val):
#     response = "This is a new blog"
#     return HttpResponse(response + val)

# def edit(request, val):
#     response = " You are now editing blog no"
#     return HttpResponse(response + val)


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

# def delete(request, val):
#     response = "Helloo I have requested you as my first request"
#     return redirect('/')

# Create your views here.



#  This is the first assignment <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,  end assignment 1
