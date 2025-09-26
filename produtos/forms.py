from django import forms
from .models import Empregos

FORMATO_BR = '%d/%m/%Y'

class EmpregosForm(forms.ModelForm):
    class Meta:
        model = Empregos
        fields = [
            "title",
            "description",
            "location",
            "type_job",
            "category",
            "last_date",
            "company_name",
            "company_description",
            "website",
            "salary",
            "vacancy",
            "filled",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Título da vaga"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "type_job": forms.Select(attrs={"class": "form-select", "class": "form-control"}),  # select automático pelos choices
            "category": forms.TextInput(attrs={"class": "form-control"}),
            "last_date": forms.DateInput(format='%d/%m/%Y', attrs={"type": "date", "class": "form-control"} ),
            "company_description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "website": forms.URLInput(attrs={"class": "form-control"}),
            "salary": forms.NumberInput(attrs={"class": "form-control"}),
            "vacancy": forms.NumberInput(attrs={"class": "form-control"}),
            "filled": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
    
 

        
    
    