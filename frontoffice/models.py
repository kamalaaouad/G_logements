from django.db import models

# Create your models here.

#Model dyal Personne
class Personne(models.Model):
    nom=models.CharField(max_length=200)
    prenom=models.CharField(max_length=200)
    def __str__(self):
        return self.nom + self.prenom
#Adresse
class Adresse(models.Model):
    ville=models.CharField(max_length=200)
    rue=models.CharField(max_length=200)
    no=models.IntegerField()
    cp=models.IntegerField()
    departement=models.IntegerField()
    def __str__(self):
        return self.ville+self.rue+self.no+self.cp+self.departement
#Bail
class Bail(models.Model):
    no=models.IntegerField()
    loyerTTC=models.FloatField()
    date_debut=models.DateField(auto_now_add=True, blank=True)
    duree=models.DurationField()
    def __str_(self):
        return self.no+self.loyerTTC+self.date_debut+self.duree
#Proprietaire
class Proprietaire(Personne):
    cne=models.CharField(max_length=200)
    def __str__(self):
        return self.cne
#Collaborateur
class Collaborateur(Personne):
    courriel=models.CharField(max_length=200)
    telephone=models.CharField(max_length=200)
    def __str__(self):
        return  self.courriel + self.telephone
    def getCourriel__():
        return self.courriel
    def getTelephone__():
        return self.telephone
#Locataire
class Locataire(Personne):
    adresse_origine=models.CharField(max_length=300)
    def __str__(self):
        return self.adresse_origine
#Logement
class Logement(models.Model):
    nbPieces=models.IntegerField()
    surface=models.FloatField()
    photo=models.CharField(max_length=200)
    loyer=models.FloatField()
    charges=models.FloatField()
    partAgence=models.FloatField()
    def __str__(self):
        return nbPieces+surface+photo+loyer+charges+partAgence
#Model dyal Maison
class Maison(models.Model):
    surface_terrain=models.FloatField()
    grenier=models.BooleanField()
    def __str__(self):
        return self.surface_terrain + self.grenier
#Model dyal Appartement
class Appartement(models.Model):
    etage=models.IntegerField()
    ascenseur=models.BooleanField()
    garage=models.BooleanField()
    def __str__(self):
        return self.etage + self.ascenseur +self.garage
