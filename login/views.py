from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from django.template import loader
from .models import Regi,State,District


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def reg(request):
    template = loader.get_template('register.html')
    states= State.objects.all().values()
    context={
        "state":states
    }
    return HttpResponse(template.render(context))

def log(request):
    email = request.POST['mail']
    password = request.POST['pass']
    if Regi.objects.filter(email=email,password=password):
        context = {
        
        'email':email,
        'password':password
    }
        template = loader.get_template('logdata.html')
        return HttpResponse(template.render(context))
    else:
        return HttpResponse("try again")
    
    

def regi(request):
    name = request.POST['name']
    address = request.POST['addr']
    gender = request.POST['gender']
    
    skills = request.POST['languages']
    email = request.POST['mail']
    password = request.POST['pass']
    reg=Regi(
        name=name,
        addres=address,
        gender=gender,
        skills=skills,
        email=email,
        password=password
        
    )
    
    reg.save()
    
    context = {
        'nam':name,
        'addr':address,
        'gender':gender,
        'languages':skills,
        'mail':email,
        'pass':password
    }
    template = loader.get_template('regdata.html')
    return HttpResponse(template.render(context))

def dist(request):
    state=request.POST['state']
    districts=District.objects.filter(state=state).values()
    print(districts)

    return JsonResponse({'values': list(districts)})