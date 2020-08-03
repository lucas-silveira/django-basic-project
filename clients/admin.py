from django.contrib import admin
from .models import Client, Document, Sale, Product

admin.site.register(Client)
admin.site.register(Document)
admin.site.register(Sale)
admin.site.register(Product)
