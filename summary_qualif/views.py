from django.shortcuts import render, redirect
from .models import ResumeCv
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView


def listResumeCV(request):
    
    resumecv = ResumeCv.objects.filter(user_id = request.user.id)
    return render(request, 'summary_qualif/profile-user.html', {'resumecv': resumecv} )

class ResumeCV_CreateView(CreateView):
    model = ResumeCv
    template_name = 'summary_qualif/register.html'
    fields = ['user', 'name', 'email', 'celphone', 'city', 'state', 'qualifications', 'courses', 
               'experiences', 'is_published']
    
    success_url = reverse_lazy('summary_qualif:listResumeCV')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cadastrar Curriculum'
        return context
    
class ResumeCV_EditView(UpdateView):
    model = ResumeCv
    template_name = 'summary_qualif/profile.html'
    fields = ['user', 'name', 'email', 'celphone', 'adress_user', 'city', 'state', 'qualifications', 'courses', 
               'experiences', 'resume_file', 'is_published']
     
    success_url = reverse_lazy('summary_qualif:listResumeCV')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cadastrar Curriculum'
        return context
    
    def get_initial(self):
        initial = super().get_initial()

        if self.request.user.id:
            initial['user'] = self.request.user.id
        return initial