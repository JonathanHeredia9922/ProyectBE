from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    
    return render(request,"appGPR/home.html" )


def tienda(request):
    
     return render(request,"appGPR/tienda.html" )


def contacto(request):
    
     return render(request,"appGPR/contacto.html" )