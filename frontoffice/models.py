from django.db import models

# Create your models here.
#Adresse
class Adresse(models.Model):
    ville=models.CharField(max_length=200)
    rue=models.CharField(max_length=200)
    no=models.IntegerField()
    cp=models.IntegerField()
    departement=models.IntegerField()
    def __str__(self):
        return self.ville+"-"+self.rue+"-"+str(self.no)+"-"+str(self.cp)+"-"+str(self.departement)
#Model dyal Personne
class Personne(models.Model):
    nom=models.CharField(max_length=200)
    prenom=models.CharField(max_length=200)
    adresse=models.ForeignKey(Adresse, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom + self.prenom

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
    adresse=models.ForeignKey(Adresse, on_delete=models.CASCADE)
    proprietaire=models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    collaborateur=models.ForeignKey(Collaborateur, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.nbPieces)+"-"+str(self.surface)+"-"+self.photo+"-"+str(self.loyer)+"-"+str(self.charges)+"-"+str(self.partAgence)
#Model dyal Maison
class Maison(Logement):
    surface_terrain=models.FloatField()
    grenier=models.BooleanField()
    def __str__(self):
        return str(self.surface_terrain)+"-"+ str(self.grenier)
#Model dyal Appartement
class Appartement(Logement):
    etage=models.IntegerField()
    ascenseur=models.BooleanField()
    garage=models.BooleanField()
    def __str__(self):
        return str(self.etage)+"-"+str(self.ascenseur)+"-"+str(self.garage)
#Bail
class Bail(models.Model):
    no=models.IntegerField()
    loyerTTC=models.FloatField()
    date_debut=models.DateField(auto_now_add=True, blank=True)
    duree=models.DurationField()
    locataire=models.ForeignKey(Locataire, on_delete=models.CASCADE)
    logement=models.ForeignKey(Logement, on_delete=models.CASCADE)
    def __str_(self):
        return str(self.no)+"-"+str(self.loyerTTC)+"-"+str(self.date_debut)+"-"+str(self.duree)