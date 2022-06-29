from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import forms
from aircraft.models import AddAirCraft

class Class(models.Model):
    name = models.CharField(max_length=10)
    price = models.DecimalField(default='100$',max_digits=4,decimal_places=2)


class add_flight(models.Model):
    source = models.CharField(max_length=100)
    To = models.CharField(max_length=100)
    check_in_date = models.DateTimeField(default=timezone.now)
    check_out_date = models.DateTimeField(default=timezone.now)
    author = models.CharField(default='Admin', max_length=10)
    plane = models.ForeignKey(AddAirCraft, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.source


Class = [('economey', 'economey'), ('first', 'first'), ('luxury','luxury'), ('premium','premium')]


class Booking(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    flight = models.ForeignKey(add_flight, null=False, on_delete=models.CASCADE)
    classes = models.CharField(max_length=10,choices=Class, default='economey')
    price = models.DecimalField(default=600,decimal_places=0,max_digits=5)
    def __str__(self):
        return str(self.user) + str(self.flight)