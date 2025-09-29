from django.shortcuts import render, redirect
from produtos.models import Empregos
from produtos.forms import EmpregosForm
from django.contrib import messages


def home(request):
    
    jobs = Empregos.objects.all()
        
    return render(request, 'produtos/partials/home.html', {'jobs': jobs} )
# Create your views here.


def registerProduct(request):
    form = EmpregosForm()
    titleform = "Cadastro de Oportunidade"
    
    if request.method == 'POST':
        form = EmpregosForm(request.POST)
        if form.is_valid(): 
            form.save()
            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('accounts:login')
        else:
            messages.error(request, form.errors.keys)
            return redirect('produtos:register')
             
    return render(request, 'produtos/register.html', {'form': form,'title' : titleform })

def listProduct(request):
     jobs = Empregos.objects.all()
     
     return render(request, 'produtos/produtos-list.html', {'jobs': jobs} )
    
    
