from django import forms
from .models import *

#Logement Form
class LogementForm(forms.ModelForm):

    class Meta:
        model=Logement
        fields = ('nbPieces','surface','photo','loyer','charges','partAgence','adresse','proprietaire','collaborateur')
        labels={
            'nbPieces':'Nombres Pieces',
            'surface':'Surface',
            'photo':'Photo',
            'loyer':'Loyer',
            'charges':'Taxe Charges',
            'partAgence':'Part Agence',
            'adresse':'Adresse',
            'proprietaire':'Proprietaire',
            'collaborateur':'Collaborateur'
        }
    def __init__(self,*args,**kwargs):
        super(LogementForm,self).__init__(*args,**kwargs)
        self.fields['adresse'].empty_label="Selectionner l'adresse"
        self.fields['photo'].required=False

#Collaborateur Form

class CollaborateurForm(forms.ModelForm):

    class Meta:
        model=Collaborateur
        fields = ('nom','prenom','adresse','courriel','telephone')
        labels={
            'nom':'Nom',
            'prenom':'Prenom',
            'adresse':'Adresse',
            'courriel':'Courriel',
            'telephone':'Telephone'
        }
    def __init__(self,*args,**kwargs):
        super(CollaborateurForm,self).__init__(*args,**kwargs)
        self.fields['adresse'].empty_label="Selectionner votre adresse"
        self.fields['telephone'].required=False

#Proprietaire Form :: ProprietaireForm


class ProprietaireForm(forms.ModelForm):

    class Meta:
        model=Proprietaire
        fields = ('nom','prenom','adresse','cne')
        labels={
            'nom':'Nom',
            'prenom':'Prenom',
            'adresse':'Adresse',
            'cne':'CNE'
        }
    def __init__(self,*args,**kwargs):
        super(ProprietaireForm,self).__init__(*args,**kwargs)
        self.fields['adresse'].empty_label="Selectionner votre adresse"