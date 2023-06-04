from django.shortcuts import render,HttpResponse

# Create your views here.


def index(request):
    return render(request,"index.html")

def storeData(request):
    data = {
        'name' : request.POST['name'],
        'location' : request.POST['location'],
        'language' : request.POST['lang'],
    }
    return render(request,"result.html",data)