from django.shortcuts import render, redirect
from.forms import contactform
from django.core.mail import EmailMessage
from django.urls import reverse

# Create your views here.
def contact (request):
    print('tipo de metodo de envio{}', request.method)
    contactfor = contactform()
    if request.method == "POST":
        contactfor= contactform(data=request.POST)
        if contactfor.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            contact = request.POST.get('contact', '')
    #enviar el correo
        email = EmailMessage(
            'la cafeteria',
            "De {} <{}>\n\n{}".format(name, email, contact),
            'no contestar',
            ['jdlascano@est.itsgg.edu.ec'],
            reply_to=[email]
        )
        try:
            email.send()
            return redirect(reverse('contact')+"?ok")
        except:
            return redirect(reverse('contact') + "?fail")
    return render(request, 'contact/contact.HTML', {'form': contactfor})