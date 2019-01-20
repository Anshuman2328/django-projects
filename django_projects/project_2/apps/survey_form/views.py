from django.shortcuts import render, HttpResponse, redirect



def index(request): 
    return render(request, 'survey_form/index.html')
    return render(request, 'survey_form/index.html', {'keywords':request.session['test']}) # this is making a new object in the render template


def field(request):
    # request.session["my_list"] = []
    
    #     "my_font" : request.POST['large_font']
        
    # if 'test' not in request.session['test']:
    #     request.session['test'] = Null
    
    # context = {
    #     'keywords': request.session['test']
        
        # 'my_font' : request.session['large_font']
    # }
    # print(f'i am {context}')

    # if my_dictionary not in session:
    # "user_color" : request.POST['color']
    # print (my_dictionary)
    # my_list.append(my_dictionary)
    if request.method == "POST":
        request.session['color'] = request.POST['color'] # the left side is a variable, right side is from the form
        request.session['test'] = request.POST['word']
        request.session["font_size"] = request.POST["large_font"]
        if "my_dictionary" not in request.session:
            request.session["my_dictionary"] = [{
            "keywords" : request.session['test'],
            "user_color" : request.session['color'],
            "user_font" : request.session["font_size"]
            }]
            return redirect("/")

        else:    
            temp_list = request.session["my_dictionary"]
            temp_list.append({"test": request.POST['word'], "color": request.POST['color'], "font_size" : request.POST["large_font"]})
            request.session['my_dictionary'] = temp_list
            # request.session["test"].append({"keywords" :request.POST['word'], "user_color" :request.POST['color']})
            # print(request.session["test"])
        # request.session['font'] = request.POST['large_font']
            return redirect('/')
    else: 
        return redirect('/')

def clear(request):
    request.session.clear()
    return redirect("/")



































    # context = {
    #     "word" : request.POST['word'],
    #     "color" : request.POST['color']
    # }
    # return render(request, "survey_form/index.html", context)
