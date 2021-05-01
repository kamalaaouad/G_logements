from django.contrib import admin
#importi l models huma lwelin
from .models import *;
# Register your models here.

admin.site.register(Adresse,AdresseAdmin)
admin.site.register(Bail,BailAdmin)
admin.site.register(Locataire, locataireAdmin)
admin.site.register(Collaborateur,CollaborateurAdmin)
admin.site.register(Proprietaire,ProprietaireAdmin)
admin.site.register(Appartement,AppartementAdmin)
admin.site.register(Maison,MaisonAdmin)
