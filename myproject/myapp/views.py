from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature = Feature.objects.all()
    return render(request,'index.html',{'feature':feature})

def counter(request):
    text = request.POST['text']
    amount = len(text.split())
    return render(request,'counter.html',{'val':amount})
