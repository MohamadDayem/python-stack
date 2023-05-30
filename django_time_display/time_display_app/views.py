from django.shortcuts import render
from time import gmtime, strftime
    
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %I:%M %p"),
    }
    return render(request,'index.html', context)

