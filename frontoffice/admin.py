from django.contrib import admin
#importi l models huma lwelin
from .models import *;
# Register your models here.
admin.site.register(Personne)
admin.site.register(Adresse)
admin.site.register(Bail)
admin.site.register(Proprietaire)
admin.site.register(Collaborateur)
admin.site.register(Locataire)
admin.site.register(Logement)
admin.site.register(Maison)
admin.site.register(Appartement)
