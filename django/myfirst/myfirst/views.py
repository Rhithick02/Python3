from django.http import HttpResponse
from django.shortcuts import render
def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')

def homepg(request):
    # return HttpResponse('This is the homepage')
    return render(request, "homepage.html")