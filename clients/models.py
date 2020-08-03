from django.db import models


class Document(models.Model):
    number = models.CharField(max_length=20)
    issuing_state = models.CharField(max_length=10)

    def __str__(self):
        return self.number


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    avatar = models.ImageField(
        upload_to='clients_avatar', null=True, blank=True)
    doc = models.OneToOneField(Document, null=True, blank=True,
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Product(models.Model):
    name = models.CharField(max_length=30)
    value = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Sale(models.Model):
    value = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    client = models.ForeignKey(
        Client, null=True, blank=True, on_delete=models.SET_NULL)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.pk
