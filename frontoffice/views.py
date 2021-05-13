from django.shortcuts import redirect, render
from .forms import LogementForm

# Create your views here.

def home(request):
    return render(request,'front/index.html')

def logements(request):
    return render(request,'logements/logements.html')

def logements_list(request):
    return  render(request,'logements/logements_list.html')

def logements_form(request):
    if request.method=='GET':
        form = LogementForm()
        return  render(request,'logements/logements_form.html',{'form':form})
    else:
        form = LogementForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/logements/list')