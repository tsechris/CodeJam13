from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def camera(r):
    if r.method == "POST":
        img_link = str(r.POST['img_link'])
        img_link = img_link[22:]
        print(img_link)



    tmp = loader.get_template('camera.html')
    return HttpResponse(tmp.render())