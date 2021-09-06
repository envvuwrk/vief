from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def gallery(request):
    return render(request, 'gallery.html')

def sponsor(request):
    return render(request, 'sponsors.html')

def designers(request):
    return render(request, 'designers.html')


def designer(request):
    return render(request, 'designer.html')



def exhibitor(request):
    return render(request, 'exhibitor.html')



def model(request):
    return render(request, 'model.html')