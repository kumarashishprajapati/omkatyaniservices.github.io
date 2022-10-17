from multiprocessing import context
from sqlite3 import Cursor
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    # return HttpResponse("This is Home Page")
    return render(request,'index.html',)
def about(request):
    return render(request,'about.html')
    #return HttpResponse("This is about Page")
def services(request):
    return render(request,'services.html')
    #return HttpResponse("This is services Page")
def contact(request):
    if request.method == "POST":
        name =  request.POST.get('name')
        phone=  request.POST.get('phone')
        email =  request.POST.get('email')
        comments =  request.POST.get('comments')
        contact=Contact(name=name,phone=phone,email=email,comments=comments,date=datetime.today())
        contact.save()

    return render(request,'contact.html')
    #return HttpResponse("This is contact Page")