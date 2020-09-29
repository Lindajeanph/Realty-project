from django.shortcuts import render, redirect
from .forms import create_new_happ_user, survey


def home(request):
    return render(request, 'HikingApp/HikingApp_Home.html')


def dailysurvey(request):
    form = survey(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('happ_home')
    return render(request, 'HikingApp/HikingApp_Survey.html', {'form': form})


def create_the_happ_user(request):
    form = create_new_happ_user(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('happ_home')
    return render(request, 'HikingApp/HikingApp_MyProfile.html', {'form': form})