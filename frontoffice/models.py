from django.db import models
from django.contrib import admin

# Create your models here.


class Personne(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom + self.prenom

    class Mata:
          ordering=["nom"]


# Adresse
class Adresse(models.Model):
    ville = models.CharField(max_length=200)
    rue = models.CharField(max_length=200)
    no = models.IntegerField()
    cp = models.IntegerField()
    departement = models.IntegerField()

    def __str__(self):
        return self.ville + self.rue + self.no + self.cp + self.departement


# Bail
class Bail(models.Model):
    no = models.IntegerField()
    loyerTTC = models.FloatField()
    date_debut = models.DateField(auto_now_add=True, blank=True)
    duree = models.DurationField()

    def __str_(self):
        return self.no + self.loyerTTC + self.date_debut + self.duree


# Proprietaire
class Proprietaire(Personne):
    cnl = models.CharField(max_length=200)

    def __str__(self):
        return self.cne


# Collaborateur
class Collaborateur(Personne):
    courriel = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)

    def __str__(self):
        return self.courriel + self.telephone

    def getCourriel__(self):
        return self.courriel

    def getTelephone__(self):
        return self.telephone


# Locataire
class Locataire(Personne):
    adresse_origine = models.CharField(max_length=300)

    def __str__(self):
        return self.adresse_origine


# Logement
class Logement(models.Model):
    nbPieces = models.IntegerField()
    surface = models.FloatField()
    photo = models.CharField(max_length=200)
    loyer = models.FloatField()
    charges = models.FloatField()
    partAgence = models.FloatField()

    def __str__(self):
        return self.nbPieces + "-" + self.surface + "-" + self.photo + self.loyer + "-" + self.charges + "-" + self.partAgence


# Model dyal Maison
class Maison(Logement):
    surface_terrain = models.FloatField()
    grenier = models.BooleanField()

    def __str__(self):
        return self.surface_terrain + self.grenier


# Model dyal Appartement
class Appartement(Logement):
    etage = models.IntegerField()
    ascenseur = models.BooleanField()
    garage = models.BooleanField()

    def __str__(self):
        return self.etage + self.ascenseur + self.garage

class locataireAdmin(admin.ModelAdmin):
    list_display = ('nom','prenom','adresse_origine')

class CollaborateurAdmin(admin.ModelAdmin):
    list_display = ('nom','prenom','courriel','telephone')

class ProprietaireAdmin(admin.ModelAdmin):
    list_display = ('nom','prenom','cnl')
class AppartementAdmin(admin.ModelAdmin):
    list_display = ('nbPieces','surface','photo','loyer','charges','partAgence','etage','ascenseur','garage')

class MaisonAdmin(admin.ModelAdmin):
    list_display = ('nbPieces','surface','photo','loyer','charges','partAgence','surface_terrain','grenier')