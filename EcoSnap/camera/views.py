from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def camera(r):
    tmp = loader.get_template('camera.html')
    return HttpResponse(tmp.render())