from django.shortcuts import render
from .models import HRdecision
from produtos.models import Empregos
from noticeboard.models import NoticeBoarforUser
from stock.models import StockGeneralJob
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.http import HttpResponseRedirect

# Create your views here.
class HRdecisionUpdateView(UpdateView):
    model = HRdecision
    template_name = 'rhmanager/rhmanager.html'
    fields = ['user', 'job', 'candidate_observation', 'rh_decision', 'rh_observation']
    
    success_url = reverse_lazy('rhmanager:listorderurs')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Realizar Analise da Solicitação'
        return context
    
    def form_valid(self, form):
        self.object = form.save()
        
        if (form.cleaned_data['rh_decision'] == "1"):  
         
            new_vacany = Empregos.objects.filter(pk=int(form.cleaned_data['job'].id)).first()
            
            Empregos.objects.filter(pk=int(form.cleaned_data['job'].id)).update(vacancy=(new_vacany.vacancy-1))

            NoticeBoarforUser.objects.create(
                 user = form.cleaned_data['user'],
                 job =  form.cleaned_data['job'],
                 approvedselection = True,
                 rh_observation = "Parabéns você foi aprovado !!!!" + " -> " + form.cleaned_data['rh_observation']
            )
            
            stockjob = StockGeneralJob.objects.filter(user_id = int(form.cleaned_data['user'].id), job_id = int(form.cleaned_data['job'].id)).first()
            
            if  stockjob is None : 
                StockGeneralJob.objects.create(
                    user = form.cleaned_data['user'],
                    job =  form.cleaned_data['job'],
                    preview = 0
                )
            else:
                StockGeneralJob.objects.filter(user_id = int(form.cleaned_data['user'].id), job_id = int(form.cleaned_data['job'].id)).update(preview= (stockjob.preview+1))
        elif (form.cleaned_data['rh_decision'] == "2"):  
            print("Aqui 2")
            NoticeBoarforUser.objects.create(
                user = form.cleaned_data['user'],
                 job =  form.cleaned_data['job'],
                 approvedselection = False,
                 rh_observation = "Você não foi aprovado ! Segue a observação da decisão" + " -> " + form.cleaned_data['rh_observation']
            )
             
        return HttpResponseRedirect(self.get_success_url())

class HRdecisionDetailView(ListView):
    model = HRdecision
    template_name = 'rhmanager/rh_managerlist.html'
    ordering = ['user']
    context_object_name = 'rhdecision'
    success_url = reverse_lazy('rhmanager:listorderurs')
    paginate_by = 10 #
    

 