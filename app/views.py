from django.shortcuts import render

# Create your views here.
from app.models import *
def retrive(request):
    lot=Topic.objects.all()
    d={'topic':lot}
    return render(request,'t1.html',d)

def web(request):
    low=Webpage.objects.all()
    d={'web':low}
    return render(request,'t2.html',d)

def Access(request):
    loa=AccessRecord.objects.all()
    d={'access':loa}
    return render(request,'t3.html',d)