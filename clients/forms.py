from django.forms import ModelForm
from .models import Client


class ClientsForm(ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'avatar']
