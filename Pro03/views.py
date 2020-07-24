from django.http import HttpResponse
from django.shortcuts import render

def main(request):
    return HttpResponse("Main Page of Django")

def home(request):
    return render(request,"first.html")

def second(request):
    return render(request,"webpages/second.html")

def third(request):
    return render(request,"webpages/third.html", context={'data':"Sunil",'name':"Kumarappa"})

def fourth(request):
    fruits = ["mango","kiwi","orange","banana","apple"]
    return render(request,"webpages/fourth.html",{'fruits':fruits})

def fifth(request):
    return render(request,"webpages/fifth.html",{'a':10,'b':5})

def urls_data(request,name):
    return HttpResponse("<h1>{}</h1>".format(name))

def ab(request,a,b):
    sum=int(a)+int(b)
    return HttpResponse(str(sum))




