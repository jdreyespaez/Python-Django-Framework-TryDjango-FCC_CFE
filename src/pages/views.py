from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    my_context = {
        "my_text": "Esta es la página de contacto.",
        "my_number": 316356
    }
    return render(request, "contact.html", my_context)
