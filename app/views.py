from django.shortcuts import render
from app.models import *
# Create your views here.
def insert_webpage(request):
    LTO=topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        TO=topic.objects.get(Topic_name=tn)
        WO=Website.objects.get_or_create (Topic_name=TO,name=na,url=ur)[0]
        WO.save()
        QSWO=Website.objects.all()
        d1={'QSWO':QSWO}
        return render (request,'display_webpage.html',d1)

    return render(request,'insert_webpage.html',d)

def select_webpage(request):
    LTO=topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        tnlist=request.POST.getlist('tn')
        print(tnlist)
        QSWO=Website.objects.none()
        for tn in tnlist:
            QSWO=QSWO|Website.objects.filter(Topic_name=tn)

        d1={'QSWO':QSWO}
       
        return render (request,'display_webpage.html',d1)

    return render(request,'select_webpage.html',d)

def checkbox(request):
    LTO=topic.objects.all()
    d={'LTO':LTO}
    return render (request,'checkbox.html',d)



def delete(request):
    LTO=topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        tn=request.POST.get('tn')
        QSWO=Website.objects.filter(Topic_name=tn).delete()
        QSWO=Website.objects.all()

        d1={'QSWO':QSWO}
       
        return render (request,'display_webpage.html',d1)

    return render(request,'delete.html',d)
    



