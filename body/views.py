from django.shortcuts import render, redirect
from django.http import HttpResponse

# HTML_STRING = """
# <h1>This is Home Page</h1>
# """

con = {'txt':'hello'}

def home(request):
    response = redirect('index.html')
    return response

# Create your views here.
def index(request):
    return render(request,'index.html',context=con)
    
def about(request):
    return render(request, 'about.html', context=con)

def contact(request):
    return render(request, 'contact.html', context=con)

def ourwork(request):
    return render(request, 'ourwork.html', context=con)

def clients(request):
    return render(request, 'clients.html')