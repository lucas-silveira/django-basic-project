from django.forms import ModelForm
from .models import Person


class PersonsForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'avatar']
