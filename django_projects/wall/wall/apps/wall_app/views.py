from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import *

def index(request):
    return render(request, 'wall_app/index.html')

def login_page(request):
    return render(request, 'wall_app/login.html')

def register_page(request):
    return render(request, 'wall_app/register.html')

def dashboard(request):
    # context = {
    #     'user_data': User.objects.all(),
    # }
    return render(request, 'wall_app/dashboard.html', { 'user_data': User.objects.all() })

def users_new(request):
    return render(request, 'wall_app/users_new.html')

def users_homepage(request, id):
    user = User.objects.filter(id = id)
    for user in user:
        context = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'id': user.id,
            'email': user.email,
            'description': user.description,
            'user_level': user.user_level,
            'created_at': user.created_at,
        }

    return render(request, 'wall_app/users_homepage.html', context)

def register(request):
    if request.POST['submit'] == 'Register' or request.POST['submit'] == 'Create':
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags = tag)
            return redirect('/register')

        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = password)
        if 'login_status' not in request.session:
            request.session['login_status'] = 1
        else:
            request.session['login_status'] = 1

        if 'user_level' not in request.session: #User does not exist
            request.session['id'] = user.id
            request.session['user_level'] = user.user_level
            return redirect('/users/show/'+str(request.session['id']))
        elif request.session['user_level'] == 2:
            request.session['id'] = user.id #User is not admin
            request.session['user_level'] = user.user_level
            return redirect('/users/show/'+str(request.session['id']))
        elif request.session['user_level'] == 1:
            return redirect('/users/show/'+str(user.id))

def login(request):
    if request.POST['submit'] == 'Login':
        user = User.objects.filter(email = request.POST['email'])
        if not user:
            messages.add_message(request, messages.INFO, 'User does not exist')
            return redirect('/login')
        else:
            for user in user:
                user_password = user.password
            if bcrypt.checkpw(request.POST['password'].encode(), user_password.encode()):
                context = {
                    'name': user.first_name,
                    'status': 'logged in',
                    'email_error': 'User does not exist'
                }
                if 'login_status' not in request.session:
                    request.session['login_status'] = 1
                else:
                    request.session['login_status'] = 1
                request.session['id'] = user.id
                request.session['user_level'] = user.user_level
                return redirect('/users/show/'+str(request.session['id']))
            else:
                messages.add_message(request, messages.INFO, 'Password is incorrect')
                return redirect('/login')

def logout(request):
    request.session['login_status'] = 0
    del request.session['id']
    del request.session['user_level']
    return redirect ('/login')

def edit(request, id): #goes to the edit page
    # user = User.objects.filter(id = id)
    # for user in user:
    context = {
        'user_data': User.objects.filter(id = id)
    }
    return render(request, 'wall_app/edit.html', context)

def edit_users(request):
    user = User.objects.get(id = request.POST['id'])
    if request.POST['submit'] == 'Save':
        user.email = request.POST['email']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.user_level = request.POST['user_level']
        user.save()
        return redirect('/dashboard')


    if request.POST['submit'] == 'Update Password':
        errors = User.objects.password_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags = tag)
            return redirect('/users/edit/'+str(user.id))

        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user.password = password
        user.save()
        return redirect('/dashboard')

    if request.POST['submit'] == 'Edit Description':
        user.description = request.POST['description']
        user.save()
        return redirect('/dashboard')

def delete(request, id):
    User.objects.get(id=id).delete()

    return redirect('/dashboard')