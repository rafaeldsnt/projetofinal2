from django.shortcuts import render, redirect
from .models import Empregos
from django.contrib.auth.models import User
from .forms import EmpregosForm
from django.contrib import messages

 
def home(request):
    
    jobs = Empregos.objects.all()
    
    total = len(jobs)
    
    return render(request, 'produtos/partials/home.html', {'jobs': jobs, 'total' : total} )
# Create your views here.

def registerProduct(request):
    titleform = "Cadastro de Oportunidade"
    if request.method == "POST":
        form = EmpregosForm(request.POST)
        if form.is_valid(): 
            form.save()
            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('accounts:login')
        else:
            messages.error(request, form.errors.keys)
            return redirect('produtos:register')
    else:
        form = EmpregosForm()
        return render(request, 'produtos/register.html', {'form': form,'title' : titleform })
    
def listProduct(request):
     jobs = Empregos.objects.all()
     
     return render(request, 'produtos/produtos-list.html', {'jobs': jobs} )
 
