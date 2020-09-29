from django.shortcuts import render


def home(request):
    return render(request, 'CatchIdentificationApp/CatchIdentification_Home.html')
