from django.shortcuts import render
#from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
    #return HttpResponse('<h1>index</h1>')

# Create your views here.
