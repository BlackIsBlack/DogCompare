# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
sys.path.append('/home/pi/DogProject')
import compare
from django.shortcuts import render

# Create your views here.

def index(request):
    compare.newDog()
    dog1Hold = compare.firstDog
    dog2Hold = compare.secondDog
    print(dog1Hold[0]["Name"], dog2Hold[0]["Name"])
    if request.method == 'POST':
        winner = request.POST.get("dogWinner")
        print(dog1Hold[0]['Name'])
        try:
            compare.SetElo(dog1Hold[0]['Name'], dog2Hold[0]['Name'], winner)

            print("Updated")
        except:
            print("Failed to update")
        compare.newDog()
        return(render(request, "index.html", {"picture1": dog1Hold[0]["Image"] , "picture2":dog2Hold[0]["Image"]}))
    return(render(request, "index.html", {"picture1": dog1Hold[0]["Image"] , "picture2":dog2Hold[0]["Image"]}))