from django.shortcuts import HttpResponse, redirect
from django.http import JsonResponse

def root(request):
    return redirect("/blogs")
def index(request):
    return HttpResponse('placeholder to later display a list of all blogs')
def news(request):
    return HttpResponse('placeholder to later display a list of all blogsjuuu')
def create(request):
    return redirect('/')
def show(request, number):
    return HttpResponse(f'placeholder to display blog number: {number}')