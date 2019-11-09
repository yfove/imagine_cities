from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'page/home.html', {})

def about(request):
    return render(request, 'page/about.html', {})

def our_work(request):
    return render (request, 'page/ourwork.html', {})

def get_involved(request):
    return render (request, 'page/getinvolved.html', {})

def contact_us(request):
    return render (request, 'page/contactus.html', {})
