from django.shortcuts import render, HttpResponse
from .models import RecycleStats

# Create your views here

def game(requests):
    entry = RecycleStats.objects.filter(user="test2")
    user = entry.get(user="test2")
    total_recycled = user.glass + user.metal + user.plastic

    return render(requests, "game.html", {"plastic": user.plastic,
                                          "glass": user.glass,
                                          "metal": user.metal,
                                          "user": user.user,
                                          "xp": user.xp,
                                          "trash": user.trash,
                                          "compost": user.compost,
                                          "daily_streak": user.daily_streak, 
                                          "total_recycled": total_recycled
                                          })
