from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from .forms import ClientsForm


def clients_list(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})


def clients_new(request):
    form = ClientsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('clients_list')
    return render(request, 'clients_form.html', {'form': form, 'button_name':
                                                 'Cadastrar'})


def clients_update(request, id):
    client = get_object_or_404(Client, pk=id)
    form = ClientsForm(request.POST or None,
                       request.FILES or None, instance=client)

    if form.is_valid():
        form.save()
        return redirect('clients_list')

    return render(request, 'clients_form.html', {'form': form, 'button_name':
                                                 'Atualizar'})


def clients_delete(request, id):
    clients = get_object_or_404(Client, pk=id)
    clients.delete()
    return redirect('clients_list')
