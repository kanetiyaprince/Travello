from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("Hello world!")
    return render(request,'index.html',{'name':'prince'})

def add(request):
    return render(request, 'add.html')

def result(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    result = val1+val2

    return render(request, 'result.html',{'answer':result})