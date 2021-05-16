from django.shortcuts import redirect, render
from .forms import *
from .models import *
# Create your views here.

def home(request):
    return render(request,'front/index.html')

#VIEWS OF :: --> "LOGEMENTS"
def logements(request):
    return render(request,'logements/logements.html')
    #LIST
def logements_list(request):
    context ={'logementsObjects':Logement.objects.all()}
    return  render(request,'logements/logements_list.html',context)
    #INSERT  && UPDATE FORM
def logements_form(request,id=0):
    if request.method=='GET':
        if id==0:
            form = LogementForm()
        else:
            logement = Logement.objects.get(pk=id)
            form = LogementForm(instance=logement)
        return  render(request,'logements/logements_form.html',{'form':form})
    else:
        if id==0:
            form = LogementForm(request.POST)
        else:
            logement = Logement.objects.get(pk=id)
            form = LogementForm(request.POST,instance=logement)
        if form.is_valid():
            form.save()
        return redirect('/logements/list')
    #DELETE 
def logements_delete(request,id=0):
    if id==0:
        return redirect('logements/list')
    else:
        logement=(Logement.objects.get(pk=id))
        logement.delete()
        return redirect('/logements/list')

## Collaborateurs Views ::
    #Collaborateur Insert && Update ::
def collaborateur_form(request,id=0):
    if  request.method=="GET":
        if id==0:
            collaborateurForm = CollaborateurForm()
        else:
            collaborateur = Collaborateur.objects.get(pk=id)
            collaborateurForm = CollaborateurForm(instance = collaborateur)
        return render(request,'Collaborateurs/collaborateurs_form.html',{'form':collaborateurForm})
    else:
        if id==0:
            collaborateurForm = CollaborateurForm(request.POST)
        else:
            collaborateur = Collaborateur.objects.get(pk=id)
            collaborateurForm = CollaborateurForm(request.POST,instance=collaborateur)
        if collaborateurForm.is_valid():
            collaborateurForm.save()
        return redirect('/logements/collaborateurs/list')
    #Collaborateur Liste :: 
def collaborateurs(request):
    context ={'collaborateurObjects':Collaborateur.objects.all()}
    return render(request,'Collaborateurs/collaborateurs_list.html',context)
    
    #Collaborateur delete ::
def collaborateur_delete(id=0):
    if id==0:
        return redirect('/logements/collaborateurs/list')
    else:
        c=(Collaborateur.objects.get(pk=id))
        Collaborateur.delete()
        return redirect('/logements/collaborateurs/list')

#Proprietaire Views :: 
    #Proprietaire Insert && Update ::
def proprietaire_form(request,id=0):
    if  request.method=="GET":
        if id==0:
            proprietaireForm = ProprietaireForm()
        else:
            proprietaire = Proprietaire.objects.get(pk=id)
            proprietaireForm = ProprietaireForm(instance = proprietaire)
        return render(request,'Proprietaires/proprietaires_form.html',{'form':proprietaireForm})
    else:
        if id==0:
            proprietaireForm = ProprietaireForm(request.POST)
        else:
            proprietaire = Proprietaire.objects.get(pk=id)
            proprietaireForm = ProprietaireForm(request.POST,instance=proprietaire)
        if proprietaireForm.is_valid():
            proprietaireForm.save()
        return redirect('/logements/proprietaires/list')
    #Proprietaire Liste :: 
def proprietaires(request):
    context ={'proprietaireObjects':Proprietaire.objects.all()}
    return render(request,'Proprietaires/proprietaires_list.html',context)
    
    #Proprietaire delete ::
def proprietaire_delete(id=0):
    if id==0:
        return redirect('/logements/proprietaires/list')
    else:
        proprietaire=(Proprietaire.objects.get(pk=id))
        proprietaire.delete()
        return redirect('/logements/proprietaires/list')