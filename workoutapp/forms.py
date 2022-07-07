from django.forms import ModelForm
from .models import itemTable, planTable

class planForm(ModelForm):
    
    class Meta:
        model = planTable 
        fields = 'day', 'category', 'exercise'


