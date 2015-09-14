from django.shortcuts import render


def sos(request):
    return render(request, 'rescue/sos.html',)
