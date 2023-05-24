from django.shortcuts import render
from django.db.models.functions import Length
# Create your views here.
from app.models import *
def retrive(request):
    lot=Topic.objects.all()
    #lot=Topic.objects.filter(topic_name='cricket')
    d={'topic':lot}
    return render(request,'t1.html',d)

def web(request):
    low=Webpage.objects.all()
    low=Webpage.objects.filter(name='Dhoni')
    low=Webpage.objects.order_by('-name')
    low=Webpage.objects.order_by(Length('name').desc())
    low=Webpage.objects.exclude(name='Dhoni')
    low=Webpage.objects.filter(name__gt='Dhoni')
    low=Webpage.objects.filter(name__lt='Dhoni')
    low=Webpage.objects.filter(name__gte='Dhoni')
    low=Webpage.objects.filter(name__lte='Dhoni')
    low=Webpage.objects.all()
    d={'web':low}
    return render(request,'t2.html',d)

def Access(request):
    loa=AccessRecord.objects.all()
    d={'access':loa}
    return render(request,'t3.html',d)

def update(request):
    Webpage.objects.filter(name='dhoni').update(url='https://msd@gmail.com')
    to=Topic.objects.get_or_create(topic_name='cricket')[0]
    to.save()
    Webpage.objects.update_or_create(name='virat',defaults={'topic_name':to,'url':'https://virat.com' })
    to=Topic.objects.get_or_create(topic_name='cricket')[0]
    to.save()
    Webpage.objects.get_or_create(name='kohli',defaults={'topic_name':to,'url':'https://kohli.com'})
    Webpage.objects.filter(name='kohli').delete()
    d={'web':Webpage.objects.all()}
    return render(request,'t2.html',d)