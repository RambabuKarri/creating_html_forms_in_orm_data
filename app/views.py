from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from app.models import *

def insert_topic(request):
    if request.method=='POST':
        topic=request.POST['topic']

        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('Insertion of Topic is Done')
    return render(request,'insert_topic.html')


def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']

        to=Topic.objects.get(topic_name=tn)
        to.save()
        wo=Webpage.objects.get_or_create(topic_name=to,name=na,url=ur)[0]
        wo.save()
        return HttpResponse('Insertion  of webpage is done')
    return render(request,'insert_webpage.html',d)


def insert_accessrecord(request):
    if request.method=='POST':
        n=request.POST['name']
        d=request.POST['date']
        a=request.POST['author']

        no=Webpage.objects.get(name=n)
    
        ao=AccessRecord.objects.get_or_create(name=no,date=d,author=a)[0]
        ao.save()
        return HttpResponse('Insertion of Access Records are Done')
    return render(request,'insert_accessrecord.html')




def retrieve_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        MSTS=request.POST.getlist('topic')
        print(MSTS)
        RWOS=Webpage.objects.none()
        for i in  MSTS:
            RWOS=RWOS|Webpage.objects.filter(topic_name=i)
        d1={'RWOS':RWOS}
        return render(request,'display_webpages.html',d1)
    return render(request,'retrieve_webpage.html',d)

def webpage_checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'webpage_checkbox.html',d)




def retrieve_access(request):
    LTO=Webpage.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        MSTS=request.POST.getlist('name')
        print(MSTS)
        RWOS=AccessRecord.objects.none()
        for i in  MSTS:
            RWOS=RWOS|AccessRecord.objects.filter(name=i)
        d1={'RWOS':RWOS}
        return render(request,'display_access.html',d1)
    return render(request,'retrieve_access.html',d)


def access_checkbox(request):
    LTO=Webpage.objects.all()
    d={'LTO':LTO}
    return render(request,'access_checkbox.html',d)















