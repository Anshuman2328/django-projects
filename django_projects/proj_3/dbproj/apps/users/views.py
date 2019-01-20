from django.shortcuts import render, HttpResponse, redirect
from.models import *

# Create your views here.
def main(request):
    return render (request,'users/index.html')

def index(request):
    context ={
        "allusers":User.objects.all()
    }

    return render(request, 'users/display.html', context)


def createuser(request):
    if request.method == 'POST':
        User.objects.create(fname=request.POST['fname'],lname=request.POST['lname'],email=request.POST['email'])
    return redirect('/display')


def showuser(request, id):
    context = {
        'id': id,
        'first_name': User.objects.get(id=id).fname,
        'last_name': User.objects.get(id=id).lname,
        'email': User.objects.get(id=id).email,
        'created_at': User.objects.get(id=id).created_at,
        'updated_at': User.objects.get(id=id).updated_at

    }

    return render(request, 'users/show.html', context)

def edituser(request, id):
    context = {
    'id': id,
    'first_name': User.objects.get(id=id).fname,
    'last_name': User.objects.get(id=id).lname,
    'email': User.objects.get(id=id).email,
    'created_at': User.objects.get(id=id).created_at,
    'updated_at': User.objects.get(id=id).updated_at

    }

    return render(request, 'users/edit.html', context)

def updateuser(request, id):
    user = User.objects.get(id=id)
    user.fname = request.POST['first_name']
    user.lname = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    # print (user)
    # print(user.first_name)

    return redirect('/showuser/'+ str(id))


def deleteuser(request, id):
    User.objects.get(id=id).delete()
    return redirect('/display')


# def updateuser(request, id):
#     context = {
#     'id': id,
#     'first_name': User.objects.get(id=id).fname,
#     'last_name': User.objects.get(id=id).lname,
#     'email': User.objects.get(id=id).email,
#     'created_at': User.objects.get(id=id).created_at,
#     'updated_at': User.objects.get(id=id).updated_at

#     }

#     return render(request, 'users/edit.html', context)
# def showuser(request):

#     return render(request, 'users/show.html')






