from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Address(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    country = models.TextField()

    def __str__(self):
        return "Address from: " + self.city
