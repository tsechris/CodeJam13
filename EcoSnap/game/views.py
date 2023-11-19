from django.shortcuts import render, HttpResponse
from .models import RecycleStats, History
import plotly.graph_objects as go
from numpy import log10
from copy import copy 

# Create your views here
def game(requests):
    name = requests.GET['name']
    entry = RecycleStats.objects.filter(user=name)
    
    if (bool(entry)):
        user = entry.get(user=name)
    else: #creates new entry in the table if new user
        RecycleStats.objects.create(user=name)
        entry = RecycleStats.objects.filter(user=name)
        user = entry.get(user=name)

    total_recycled = user.glass + user.metal + user.plastic
    level = round((100*log10(user.xp/20 + 10) - 100), 2)
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
    a = get_total_recycled_by_day()
    entry = RecycleStats.objects.filter(user="test2")
    user = entry.get(user="test2")

    generate_donut(user)

    return render(requests, "test.html", {"test": History.objects.filter(user = "user2"), "a": a})


def generate_donut(user):
    labels = ['Plastic','Metal','Glass','Paper', 'Compost', 'Trash']
    values = [user.plastic, user.metal, user.glass, user.paper, user.compost, user.trash]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    fig.update_traces(textposition='inside')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    fig.write_image('./game/static/donut.png')


def get_total_recycled_by_day():
    data = History.objects.filter(user = "test2")
    day_counter = 0
    accumulator = {}
    material_counter = {"plastic": 0, "metal": 0, "paper": 0, "glass": 0, "compost": 0, "trash": 0}

    for entry in data.iterator():
        if not (entry.item in material_counter.keys()):
            continue
        if accumulator.get(entry.date.isoformat()) != None:
            value = accumulator[entry.date.isoformat()]
            value[entry.item] += 1
        else:
            accumulator[entry.date.isoformat()] = copy(material_counter)
            value = accumulator[entry.date.isoformat()]
            value[entry.item] += 1

    return accumulator
