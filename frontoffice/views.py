from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request,'front/index.html')

def logements(request):
    return render(request,'logements/logements.html')

def logements_list(request):
    return  render(request,'logements/logements_list.html')