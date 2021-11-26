from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request) :
    #return HttpResponse('index')
    return render(request, 'index.html')
def academics(request) :
    #return HttpResponse('index')
    return render(request, 'academics.html')
def labs(request) :
    #return HttpResponse('index')
    return render(request, 'labs.html')
def committee(request) :
    #return HttpResponse('index')
    return render(request, 'committee.html')
def gallery(request) :
    #return HttpResponse('index')
    return render(request, 'gallery.html')
def hostel(request) :
    #return HttpResponse('index')
    return render(request, 'hostel.html')
def placements(request) :
    #return HttpResponse('index')
    return render(request, 'placements.html')
def alumni(request) :
    #return HttpResponse('index')
    return render(request, 'alumni.html')
def library(request) :
    #return HttpResponse('index')
    return render(request, 'library.html')
def about(request) :
    #return HttpResponse('index')
    return render(request, 'about.html')
def contact(request) :
    #return HttpResponse('index')
    return render(request, 'contact.html')