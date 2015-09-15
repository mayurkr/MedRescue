from django.shortcuts import render
from .forms import PostForm
from django.utils import timezone
from .models import Patient, Ambulance
from django.http import HttpResponse
from django.core.mail import send_mail
import googlemaps


def sos(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.called_time = timezone.now()
            post.save()
            ambs = Ambulance.objects.all().filter(available='Y')
            if (len(ambs) == 0):
                return HttpResponse("ambulance unavailable")
            gmaps = googlemaps.Client(
                key='AIzaSyCjLvrq1DnmWJy8ZqlXNjsIy9HCQ8UgWlw ')
            duration_list = []
            amb_list = {}
            for i in ambs:
                result = gmaps.distance_matrix(
                    (i.latitude, i.longitude), (post.latitude, post.longitude))
                if (result['status'] == 'OK'):
                    # duration_list.append(
                    #     result['rows'][0]['elements'][0]['duration']['value'])
                    amb_list[i.pk] = result['rows'][0][
                        'elements'][0]['duration']['value']
            best_time = min(amb_list, key=amb_list.get)
            best_amb = Ambulance.objects.get(pk=best_time)
            send_mail('medical emergency',
                      "Coordnates are {0} {1}".format(
                          post.latitude, post.longitude), 'from@example.com',
                      ['mayur@mayur.xyz'], fail_silently=False)
            best_amb.available='N'
            best_amb.save()

            return HttpResponse("Help is on the way !!")

    else:
        return render(request, 'rescue/sos.html',)
