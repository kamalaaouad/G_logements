from django.conf.urls import url
from frontoffice.views import *
from django.urls import path
from . import views
urlpatterns=[
   path('',views.logements),
   path('list/',views.logements_list),
   path('form/',views.logements_form)
]