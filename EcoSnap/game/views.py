from django.shortcuts import render, HttpResponse
from .models import RecycleStats
from numpy import log10

# Create your views here
def game(requests):
    entry = RecycleStats.objects.filter(user="test2")
    user = entry.get(user="test2")
    total_recycled = user.glass + user.metal + user.plastic
    level = 100*log10(user.xp/20 + 10) - 100

    glass_emission = user.glass * 302 # average CO2 saved from recycling a glass bottle is 302g
    metal_emission = user.metal * 99 # average CO2 save from recycling an aluminium can is 99g
    paper_emission = user.paper * 5 # average CO2 save from recycling paper is 5g
    plastic_emission = user.plastic * 40 # average CO2 save from a plastic bottle is 41g
    total_emission = (glass_emission + metal_emission + paper_emission + plastic_emission)/1000; 

    return render(requests, "game.html", {"plastic": user.plastic,
                                          "glass": user.glass,
                                          "metal": user.metal,
                                          "paper": user.paper,
                                          "user": user.user,
                                          "xp": user.xp,
                                          "trash": user.trash,
                                          "compost": user.compost,
                                          "daily_streak": user.daily_streak, 
                                          "total_recycled": total_recycled,
                                          "level": level,
                                          "total_emission": total_emission})


def test(requests):
    return HttpResponse("Hello World")
