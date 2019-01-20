from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, UserManager
import bcrypt

def routetomain(request):
    return redirect('/')

def index(request):
    return render(request, 'users/index.html')
    # This is Ash's home page where I have rendered a template inviting people to join. 
    # Simply renders the template for user registration and log in to the system


def register(request):
    if request.method=='POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/main')
        else:
            hashedpw = bcrypt.hashpw(request.POST['pwd'].encode(), bcrypt.gensalt())
            just_registered = User.objects.create(fname = request.POST['fname'], lname = request.POST['lname'], email=request.POST['email'], password=hashedpw.decode())
            request.session['username'] = just_registered.fname
            request.session['user_id'] = just_registered.id
        return redirect('/travels')
    return redirect('/')

def login(request):
    if request.method=='POST':
        user_logging_in = User.objects.filter(email=request.POST['lemail'])
        if len(user_logging_in) == 0:
            messages.error(request, "No matching user")
        elif not bcrypt.checkpw(request.POST['lpwd'].encode(), user_logging_in[0].password.encode()):
            messages.error(request, "Passwords do not match")
        else:
            request.session['username'] = user_logging_in[0].fname
            request.session['user_id'] = user_logging_in[0].id
            messages.error(request,'Successfully logged in ')
    return redirect('/travels')

def home(request):
    if not 'user_id' in request.session:
        messages.add_message(request, messages.INFO, "You need to log in or register first.", extra_tags = 'login')
        return redirect('/main')
    context = {
        'trips': User.objects.get(id=request.session['user_id']).trips.all(),
        'all_trips': Trip.objects.exclude(users = request.session['user_id'])
    }
    return render(request, 'trips/travels.html', context)




def logout(request):
    request.session.clear()
    messages.add_message(request, messages.INFO, "You have been logged out.", extra_tags='logout')
    return redirect('/')
# def register(request):
#     errors = User.objects.basic_validator(request.POST)
#     if len(errors):
#         for key,value in errors.items():
#             messages.error(request, error, extra_tags=tag)
#     else:
#         pwhash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
#         user = User.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], email = request.POST['email'], password = pwhash)
#         request.session['name'] = request.POST['fname']
#         request.session['user_id'] = user.id
#         messages.add_message(request, messages.INFO, "Welcome aboard, {}! This is your travel dashboard where you can plan your own trips and join other trips. Safe travels!".format(request.session['name']), extra_tags='newcomer')
#         return redirect('/travels')
#     return redirect('/')
    # If there are errors, they will display as dismissable alerts
    # on the homepage, otherwise it will proceed, add, and welcome the user

# def login(request):
#     errors = User.objects.login_validator(request.POST)
#     if len(errors):
#         for tag,error in errors.items():
#             messages.error(request, error, extra_tags=tag)
#         return redirect('/')
#     else:
#         request.session['name'] = User.objects.get(email=request.POST['email']).first_name
#         request.session['user_id'] = User.objects.get(email=request.POST['email']).id
#         return redirect('/travels')
    # If there are errors, they will display as dismissable alerts
    # on the homepage, otherwise it will proceed and login in the user
    # Logs the user out by clearing the session and redirecting to the login page
    # Also displays a dismissable alert that the user has logged out