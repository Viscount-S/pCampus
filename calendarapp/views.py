from django.shortcuts import render

# Create your views here.

def calendarapp(request):
    return render(request,'calendarapp/calapp.html', context=None)
