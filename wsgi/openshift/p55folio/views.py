from django.shortcuts import render_to_response

def home(request):
     return render_to_response('home/home.html')

def fuel(request):
    return render_to_response('home/fuel.html')

def moire(request):
    return render_to_response('home/moire.html')

def fractal(request):
    return render_to_response('home/fractal.html')
