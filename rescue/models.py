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
    name = models.CharField(default="", max_length=30, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    called_time = models.DateTimeField(default=timezone.now)
    status = (
        ('Y', 'Attended'),
        ('N', 'Unattended'),
    )
#    attended = models.CharField(max_length=1, choices=status, default='N')
    ambulance = models.ForeignKey(Ambulance, null=True, blank=True,)

    def __str__(self):
        if self.ambulance:
            return str(self.pk) + " attended by" + self.ambulance.name
        else:
            return str(self.pk)
