from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'page/home.html', {})

def about(request):
    return render(request, 'page/about.html', {})

def our_work(request):
    return render (request, 'page/ourwork.html', {})

def support_us(request):
    return render (request, 'page/getinvolved.html', {})

def contact_us(request):
    return render (request, 'page/contactus.html', {})

def our_team(request):
    return render (request, 'page/ourteam.html', {})

def values(request):
    return render (request, 'page/values.html', {})

def white_paper(request):
    return render (request, 'page/whitepaper.html', {})

def fund_development(request):
    return render (request, 'page/funddevelopment.html', {})