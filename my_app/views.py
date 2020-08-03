from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html', {'name':'Rustam'})

def add(request):
    # taking two numbers
    val1=request.POST["num1"]
    val2=request.POST["num2"]
    # simple python calculations
    res=int(val1)+int(val2)
    # rendering a web page
    return render(request, 'result.html', {'result':res})
