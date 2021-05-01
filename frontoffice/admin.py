from django.contrib import admin

# Register your models here.
from frontoffice.models import *

admin.site.register(Locataire, locataireAdmin)
admin.site.register(Collaborateur,CollaborateurAdmin)
admin.site.register(Proprietaire,ProprietaireAdmin)
admin.site.register(Appartement,AppartementAdmin)
admin.site.register(Maison,MaisonAdmin)