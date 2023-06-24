from django.shortcuts import render

# Create your views here.
from app1.models import *
def display_topics(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'display_topics.html',d)
def display_webpages(request):
    webpages=Webpage.objects.all()
    d1={'webpages':webpages}
    return render(request,'display_webpages.html',d1)
def display_records(request):
    records=Record.objects.all()
    d2={'records':records}
    return render(request,'display_records.html',d2)