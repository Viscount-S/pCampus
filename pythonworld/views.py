from django.shortcuts import render

# Create your views here.

def pythonworld(request):

    context = {'value': None}

    return render(request,'pythonworld/index.html',context)


def courses(request):

    context = {'value': None}

    return render(request,'pythonworld/courses.html',context)