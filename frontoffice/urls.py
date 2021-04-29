from django.conf.urls import url
from frontoffice.views import *

urlpatterns=[
   url(r'^$',view=home)
]