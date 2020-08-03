from django.urls import path
from .views import clients_list, clients_new, clients_update, clients_delete

urlpatterns = [
    path('/', clients_list, name="clients_list"),
    path('/new', clients_new, name="clients_new"),
    path('/update/<int:id>', clients_update, name="clients_update"),
    path('/delete/<int:id>', clients_delete, name="clients_delete"),
]
