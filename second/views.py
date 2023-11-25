from django.shortcuts import render
from django.http import HttpResponse
from second.models import Contact
from second.models import Contact2
from second.models import orderinfo
# Create your views here.
def launch(request):
    # set variable jo template m bhejte hai
    context={
        'variable':"this is sent"
    }
    return render(request,"home.html",context)
def about(request):
    return render(request,"about.html")
    #return HttpResponse("About us")
def services(request):
    return render(request,"services.html")
    #return HttpResponse("services")
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        contact=Contact(name=name, email=email, phone=phone)
        contact.save()
    return render(request,"contact.html")
    #return HttpResponse("contacts")
def success(request):
    name=request.GET['user']
    return HttpResponse("LOGIN SUCCESSFUL...!!WELCOME {}".format(name))
def web2(request):
    if request.method=="POST":
        name2=request.POST.get('name2')
        email2=request.POST.get('email2')
        phone2=request.POST.get('phone2')
        web2=Contact2(name2=name2, email2=email2, phone2=phone2)
        web2.save()
    return render(request,"index.html")
def zomato(request):
     if request.method=="POST":
            uname=request.POST.get('uname')
            date=request.POST.get('date')
            email=request.POST.get('email')
            number=request.POST.get('number')
            Restaurant=request.POST.get('Restaurant')
            drinks=request.POST.get('drinks')
            soups=request.POST.get('soups')
            dish=request.POST.get('dish')
            take=request.POST.get('take')
            homed=request.POST.get('homed')
            zomato=orderinfo(uname=uname,date=date,email=email,number=number,Restaurant=Restaurant,drinks=drinks,soups=soups,dish=dish,take=take,homed=homed)
            zomato.save()
     return render(request,"zomato.html")

def showdata(request):
    resultdisplay=Contact2.objects.all()
    return render(request,"formdata.html",{'Contact2':resultdisplay})