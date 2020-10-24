from django.shortcuts import render
from.models import services as a

# Create your views here.
def services (request ):
    service = a.objects.all()
    return render(request, 'services/services.HTML', {'service': service})