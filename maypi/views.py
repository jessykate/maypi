from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from time import sleep
from os import system
import json

def home(request):
   if request.method == 'POST':
      action = request.POST.get("action")
      if action == 'Alert':
         ding()
      if action == 'Unlock':
         unlock()

   return render(request, "home.html", {})

def pincode(request):
    if request.method == 'POST':
        pin = json.loads(request.body)["pin"]
        if pin == "1234":
            unlock()

		return HttpResponse(200)
	return HttpResponse(500)
	


def ding() :
   system("/usr/local/bin/gpio -p write 201 1")
   sleep(0.15)
   system("/usr/local/bin/gpio -p write 201 0")

def unlock():
   system("/usr/local/bin/gpio -p write 200 1")
   sleep(5)
   system("/usr/local/bin/gpio -p write 200 0")
