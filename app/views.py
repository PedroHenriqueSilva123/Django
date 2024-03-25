from django.shortcuts import render


def index(request):
    return render(request,'app/index.html')

def sobre(request):
    return render(request,'app/sobre.html')

def contato(request):
    return render(request,'app/contato.html')

def bulyn(request):
    return render(request,'app/bulyn.html')

def criadores(request):
    return render(request,'app/criadores.html')

def oquee(request):
    return render(request,'app/oquee.html')