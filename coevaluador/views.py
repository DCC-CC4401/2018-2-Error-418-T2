from django.shortcuts import render


def index(request):
    return render(request, 'coevaluador/index.html')

def LandingPagePersonaNat(request):
    return render(request, 'coevaluador/LandingPagePersonaNat.html')

def LandingPageEqD(request):
    return render(request, 'coevaluador/LandingPageEqD.html')