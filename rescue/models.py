from django.db import models
from django.utils import timezone


class Ambulance(models.Model):
    name = models.CharField(max_length=30)
    operator = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()
    availabilty = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    available = models.CharField(max_length=1, choices=availabilty)

    def __str__(self):
        return self.name + " " + self.available


class Patient(models.Model):
    name = models.CharField(default="", max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()
    called_time = models.DateField(default=timezone.now)
    choices = (
        ('Y', 'Attended'),
        ('N', 'Unattended'),
    )
    attended = models.CharField(max_length=1, choices=choices, default='N')
    ambulance = models.ForeignKey(Ambulance, null=True)

    def __str__(self):
        if self.attended == 'Y':
            return self.pk, " attended by" + self.ambulance.name
        else:
            return self.pk
