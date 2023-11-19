from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(r):
    print(r)
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
    tmp = loader.get_template('insights.html')
    return HttpResponse(tmp.render({"name": userName}))

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

