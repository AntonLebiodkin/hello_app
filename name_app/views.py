# coding=UTF-8
from __future__ import unicode_literals

import random
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    return render(request, 'name_app/index.html')


epithets = ["грустный", "старина", "хуёвый"]
current_name = ""
current_epithet = {}

def set_name(request):
    global current_name
    global current_epithet
    name = request.GET["name"]
    if current_name == name:
        return HttpResponse('Рад тебя видеть снова ' + current_epithet + ' ' + current_name)
    else:
        current_name = request.GET["name"]
        new_epithet = random.choice(epithets)
        while current_epithet == new_epithet:
            new_epithet = random.choice(epithets)
        current_epithet = new_epithet
        return HttpResponse('Рад тебя видеть ' + new_epithet + ' ' + current_name)