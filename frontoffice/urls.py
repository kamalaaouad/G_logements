from django.conf.urls import url
from frontoffice.views import *
from django.urls import path
from . import views
urlpatterns=[
   path('',views.logements),
   #Authentification URLS ::
   path('registration',views.Userreg,name="Reg"),
   path('login',views.LoginPage,name="LoginPage"),
   path('logout',views.Logout,name="Logout"),
   #Logements URLS ::
   path('list/',views.logements_list, name="logementList"),
   path('form/',views.logements_form,name="logementInsert"),
   path('<int:id>/',views.logements_form,name="logementUpdate"),
   path('delete/<int:id>/',views.logements_delete,name="logementDelete"),
   #Collaborateurs URLS ::
   path('collaborateurs/form/',views.collaborateur_form,name="collaborateurInsert"),
   path('collaborateurs/list',views.collaborateurs,name='collaborateurList'),
   path('collaborateurs/<int:id>/',views.collaborateur_form,name="collaborateurUpdate"),
   path('collaborateurs/delete/<int:id>/',views.collaborateur_delete,name="collaborateurDelete"),
   #Proprietaire URLS ::
   path('proprietaires/form/',views.proprietaire_form,name="proprietaireInsert"),
   path('proprietaires/list',views.proprietaires,name='proprietaireList'),
   path('proprietaires/<int:id>/',views.proprietaire_form,name="proprietaireUpdate"),
   path('proprietaires/delete/<int:id>/',views.proprietaire_delete,name="proprietaireDelete"),
]