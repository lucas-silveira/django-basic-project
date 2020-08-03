from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonsForm


def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'persons.html', {'persons': persons})


def persons_new(request):
    form = PersonsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('persons_list')
    return render(request, 'persons_form.html', {'form': form, 'button_name':
                                                 'Criar Person'})


def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonsForm(request.POST or None,
                       request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('persons_list')

    return render(request, 'persons_form.html', {'form': form, 'button_name':
                                                 'Atualizar Person'})


def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    person.delete()
    return redirect('persons_list')
