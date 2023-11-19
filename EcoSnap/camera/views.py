import pathlib
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from game.models import RecycleStats
import plotly.graph_objects as go

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

import torch
from PIL import Image
from .convert import base64toPIL

import torchvision.transforms.v2 as v2
import torch.nn as nn
import torch.nn.functional as F

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.dropout = nn.Dropout(0.7)
        self.conv1 = nn.Conv2d(3, 20, kernel_size=(5, 5))
        self.conv2 = nn.Conv2d(20, 50, kernel_size=(5, 5))
        self.fc1 = nn.Linear(50*53*53, 128)
        self.fc2 = nn.Linear(128, 10)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=(2, 2), stride=(2, 2))
        self.logSoftMax = nn.LogSoftmax(dim=1)
    
    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = self.dropout(x)
        x = self.pool(self.relu(self.conv2(x)))
        x = torch.flatten(x, 1)
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return self.logSoftMax(x)

def predictImage(imgStr, modelPath):
    transformer = v2.Compose([
    v2.ToImage(),
    v2.ToDtype(torch.uint8, scale=True),
    v2.Resize(size=(224, 224), antialias=True),
    v2.ToDtype(torch.float32, scale=True),  # Normalize expects float input
    v2.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]),
    ])
    # img = Image.open(imgPath).convert('RGB')
    img = base64toPIL(imgStr).convert('RGB')
    tensor = transformer(img)
    padding = torch.zeros(size=(64, 3, 224, 224))
    padding[0] = tensor
    tensor = padding

    model = CNN()
    model.load_state_dict(torch.load(modelPath, map_location=torch.device('cpu')))
    model.eval()

    _, prediction = torch.max(model(tensor), 1)
    return prediction[0]

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
        path = pathlib.Path.cwd() / 'camera/model_3.pt'
        c = predictImage(img_link, path)
        print("Classfier")
        print("id:", c)

        recyclable_status = ""
        if c == 1:
            recyclable_status = "compostable"
        elif c==8:
            recyclable_status = "trash"
        else:
            recyclable_status = "recyclable"

        entry = RecycleStats.objects.filter(user=userName)
        if (bool(entry)):
            user = entry.get(user=userName)
        else: #creates new entry in the table if new user
            RecycleStats.objects.create(user=userName)
            entry = RecycleStats.objects.filter(user=userName)
            user = entry.get(user=userName)

        #Updates the database based on the returned ID
        if c==1: #compost
            user.compost += 1 
        elif c==2 or c==4 or c==9: #glass
            user.glass += 1
        elif c==3 or c==6: #paper
            user.paper += 1
        elif c==5: #metal
            user.metal += 1
        elif c==7: #plastic
            user.plastic += 1
        elif c==8: #trash
            user.trash += 1
        user.save() #save to database

        userName = r.POST['name']
        return render(r, "base.html", {"name":userName, "recyclable_status": recyclable_status})


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

    glass_emission = user.glass * 302 # average CO2 saved from recycling a glass bottle is 302g
    metal_emission = user.metal * 99 # average CO2 save from recycling an aluminium can is 99g
    paper_emission = user.paper * 5 # average CO2 save from recycling paper is 5g
    plastic_emission = user.plastic * 40 # average CO2 save from a plastic bottle is 41g
    total_emission = (glass_emission + metal_emission + paper_emission + plastic_emission)/1000; 

    fig.write_image('./camera/static/donut.png')

    #tmp = loader.get_template('insights.html')
    #return HttpResponse(tmp.render({"name": userName}))
    #return HttpResponse(userName)
    return render(r, "insights.html", {"name": userName, "total_emission": total_emission})

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

