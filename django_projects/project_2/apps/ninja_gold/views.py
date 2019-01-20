from django.shortcuts import render, redirect, HttpResponse
import random
from datetime import datetime

def index(request):
    if "count" not in request.session or "messages" not in request.session:
        request.session["count"] = 0
        request.session["messages"] = []
    return render(request, "ninja_gold/index.html")

def process(request):
    if request.method =='POST':
        if request.POST["location"] == "farm":
            gold = random.randrange(1,21)
            request.session["messages"].append('You have earned ' + str(gold) + 'Gold !!!!! from the' + request.POST["location"] + 'on' + str(datetime.now().strftime("%Y-%m-%d %H:%M")))

        elif request.POST["location"] == "house":
            gold = random.randrange(1,6)
            request.session["messages"].append('You have earned ' + str(gold) + " " +'Gold !!!!! from the' + request.POST["location"] + 'on' + str(datetime.now().strftime("%Y-%m-%d %H:%M")))

        elif request.POST["location"] == "cave":
            gold = random.randrange(1,4)
            request.session["messages"].append('You have earned ' + '  ' +  str(gold) + ' Gold !!!!! from the' + request.POST["location"] + 'on' + str(datetime.now().strftime("%Y-%m-%d %H:%M")))

        elif request.POST["location"] == "casino":
            gold = random.randrange(-50,50)
            if gold >= 0:
                request.session["messages"].append('You have entered Casino!!!! and  earned ' + str(gold) + 'Gold !!!!! on' + str(datetime.now().strftime("%Y-%m-%d %H:%M")))
            else:
                request.session["messages"].append('You have entered Casino!!!! and  LOST ' + str(gold) + 'Gold !!!!! ----- Ouch ------- on' + str(datetime.now().strftime("%Y-%m-%d %H:%M")))
        request.session["count"] += gold
    return redirect('/')


def reset(request):
    if request.method == "POST":
        request.session['count'] = 0
        request.session['messages'] = []
    return redirect('/')





































































# def process_money(request):
#     if request.method == "POST":
#         if request.POST['building'] == 'farm':
#             gold = random.randint(10, 21)
#             request.session['activities'].append('You have earned ' + str(gold) + ' gold from the ' + request.POST['building'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

#         elif request.POST['building'] == 'cave':
#             gold = random.randint(5, 11)
#             request.session['activities'].append('You have earned ' + str(gold) + ' gold from the ' + request.POST['building'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

#         elif request.POST['building'] == 'house':
#             gold = random.randint(2,6)
#             request.session['activities'].append('You have earned ' + str(gold) + ' gold from the ' + request.POST['building'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

#         elif request.POST['building'] == 'casino':
#             gold = random.randint(-50, 51)
#             if gold >= 0:
#                 request.session['activities'].append('Entered a casino and earned ' + str(gold) +' gold' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
#             else:
#                 request.session['activities'].append('Entered a casino and lost ' + str(gold) + ' gold... Ouch...' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

#         request.session['total_gold'] += gold

#     return redirect('/')












# def index(request):
#     if 'total_gold' not in request.session or 'activities' not in request.session:
#         request.session['total_gold'] = 0
#         request.session['activities'] = []
#     return render(request, 'ninja_gold/index.html')











# $$$$$$$$$$$$$$$$$$$$$$$$ my tries $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$





#     # response "This is my first ninja gold assignment"
#     # return HttpResponse("this is my first ninja gold assignment and I have combined two apps in one project this time and i am going to try to complete ninja gold today")



# from django.shortcuts import render, HttpResponse, redirect
# from time import gmtime, strftime
# from datetime import datetime
# import random
# # now = datetime.datetime.now()
# # Create your views here


# def index(request):
#     if "count" not in request.session:
#         request.session["count"] = 0
#     if "messages" not in request.session:
#         request.session["messages"] = []
#     return render(request, "ninja_gold/index.html")

# def process(request):
#     # if request.POST["location"] == "farm":
#     #     farm_gold = random.randrange(1,21)
#     #     request.session["count"] += farm_gold
#     #     farm_message = (f"you have earned {str(farm_gold)} in this visit on ")
#     #     request.session["messages"] = farm_message
#     #     request.session["farm_gold"] = farm_gold
#     # elif request.POST["location"] == "house":
#     #     house_gold = random.randrange(1,11)
#     #     request.session["count"] += house_gold
#     #     house_message = (f"you have earned {str(house_gold)} in this visit on ")
#     #     request.session["messages"] = house_message
#     #     request.session["house_gold"] = house_gold
#     if request.POST["location"] == "casino":
#         casino_gold = random.randrange(-150,200)
#         if casino_gold < 0:
#             casino_message = (f" Ouch !!!!! you have lost {str(casino_gold)} in this visit on ")
#         else:
#             casino_message = (f" Great !!!!! you have lost {str(casino_gold)} in this visit on ")

#         request.session["count"] += casino_gold
#         request.session["messages"].append(casino_message)
#         request.session["casino_gold"] = casino_gold

#     return redirect('/')

# def clear(request):
#     request.session["count"] = 0
#     return redirect('/')
    





















#     # if request.method == "POST":
#     #     request.session["farm"] = request.POST["farm"]
#     # if "farm" not in session:
#     #     request.session["farm"] = request.method
