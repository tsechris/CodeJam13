from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from game.models import RecycleStats
import plotly.graph_objects as go

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(r):
    print(r)
    if r.method == "POST":
        userName = r.POST['name']
    if r.method == "GET":
        userName = r.GET['name']

    return render(r, "base.html")

@csrf_exempt
def camera(r):
    print("camera")
    # print(r.POST['name'])

    if r.method == "POST":
        userName = r.POST['name']
    if r.method == "GET":
        userName = r.GET['name']

    if r.method == "POST":
        img_link = str(r.POST['img_link'])
        img_link = img_link[22:]
        print(img_link)
        userName = r.POST['name']
        return render(r, "base.html", {"name":userName})



    tmp = loader.get_template('camera.html')
    return HttpResponse(tmp.render({"name": userName}))

def insights(r):
    userName = r.GET['name']
    
    entry = RecycleStats.objects.filter(user=userName)
    if (bool(entry)):
        user = entry.get(user=userName)
    else: #creates new entry in the table if new user
        RecycleStats.objects.create(user=userName)
        entry = RecycleStats.objects.filter(user=userName)
        user = entry.get(user=userName)

    labels = ['Plastic','Metal','Glass','Paper', 'Compost', 'Trash']
    values = [user.plastic, user.metal, user.glass, user.paper, user.compost, user.trash]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    fig.update_traces(textposition='inside')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    fig.write_image('./camera/static/donut.png')

    #tmp = loader.get_template('insights.html')
    #return HttpResponse(tmp.render({"name": userName}))
    #return HttpResponse(userName)
    return render(r, "insights.html", {"name": userName})

@csrf_exempt
def signin(r):
    if r.method == "POST":
        print("Signed")
        print(r.POST)
        name = str(r.POST['name'])
        tmp = loader.get_template('camera.html')
        return HttpResponse(tmp.render({"name": name}))

        # return render(r, "base.html", {"name": name} )

    return render(r, "signin.html")

import requests
@csrf_exempt
def api(r):
    if r.method == "POST":
        print("")
        r2 = requests.get("https://wttr.in")
        print(r2)
        # print(r2.content)
        print(r2.text)
        

        return render(r, "api.html" , {"content": r2.text})

    return render(r, "api.html")

