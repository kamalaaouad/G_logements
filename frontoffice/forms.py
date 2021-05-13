from django import forms
from .models import Logement
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