from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from django.template import loader
from UI.forms import MissionForm


def postmission(request):

   if request.method=="POST":

            miFormulario=MissionForm(request.POST)

            if MissionForm.is_valid():

                return render(request, "missionplanning.html", {"form":miFormulario})
                          

            else: render(request, "missionplanning.html", {"form":miFormulario})

   else: miFormulario=MissionForm()

   return render(request, "missionplanning.html", {"form":miFormulario})
