from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

import torch
from PIL import Image
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

def predictImage(imgPath, modelPath):
    transformer = v2.Compose([
    v2.ToImage(),
    v2.ToDtype(torch.uint8, scale=True),
    v2.Resize(size=(224, 224), antialias=True),
    v2.ToDtype(torch.float32, scale=True),  # Normalize expects float input
    v2.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]),
    ])
    img = Image.open(imgPath).convert('RGB')
    tensor = transformer(img)

    model = CNN()
    model.load_state_dict(torch.load(modelPath))
    model.eval()

    _, prediction = torch.max(model(tensor), 1)
    return prediction.item()

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

