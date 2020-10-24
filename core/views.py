from django.shortcuts import render

# Create your views here.
def index (request ):
    return render(request, 'core/index.html', {})

def about (request ):
    return render(request, 'core/about.HTML', {})



def sample (request ):
    return render(request, 'core/sample.HTML', {})

def store (request ):
    return render(request, 'core/store.HTML', {})