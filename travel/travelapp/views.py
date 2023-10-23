from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Place
# Create your views here.
def Hello_world(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'result':obj})

def demo(request):
    return render(request,'logineg.html')