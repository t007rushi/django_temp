from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = 'rushikesh'
    return render(request,'index.html',{'name':name}) 

def counter(request):
    text = request.POST['text']
    amount = len(text.split())
    return render(request,'counter.html',{'val':amount})    