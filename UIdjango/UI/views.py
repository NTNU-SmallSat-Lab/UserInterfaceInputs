# As many view functions as different pages/urls the webpage has.

from django.shortcuts import render # Import the required libraries
from UI.forms import MissionForm


def postmission(request):

   if request.method=="POST":

            miFormulario=MissionForm(request.POST)

            if MissionForm.is_valid():

                return render(request, "missionplanning.html", {"form":miFormulario})
                          

            else: render(request, "missionplanning.html", {"form":miFormulario})

   else: miFormulario=MissionForm()

   return render(request, "missionplanning.html", {"form":miFormulario})   #Rendering the request using the html template from the next listing
