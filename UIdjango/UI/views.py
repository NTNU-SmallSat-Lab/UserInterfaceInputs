from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from django.template import loader
from UI.forms import MissionForm



#def formulario(request):

#Form1=MissionForm.template

#return render(request, "planning.html", {"form":Form1})

def postmission(request):

   if request.method=="POST":

            miFormulario=MissionForm(request.POST)

            if MissionForm.is_valid():

                return render(request, "missionplanning.html", {"form":miFormulario})
                            # info=MissionForm.cleaned_data

                        # return render((request, gracias))

            else: render(request, "missionplanning.html", {"form":miFormulario})

   else: miFormulario=MissionForm()

   return render(request, "missionplanning.html", {"form":miFormulario})

    #doc_externo=open("C:/Users/scarc/OneDrive/Desktop/UIdjango/UI/templates/missionplanning.html")

    #The external document now is saved inside that variable

    #tpt=Template(doc_externo.read())

    #doc_externo.close()

    #doc_externo=loader.get_template('missionplanning.html')

    #ctx=Context()

    #document=doc_externo.render({})


