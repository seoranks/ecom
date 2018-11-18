from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect
from mylink.models import Products


def myDisplayFunc(request):
        products = Products(first_name = "ramesh",last_name = "gupta")
        pro = Products.objects.all()
        return render(request,"link.html",{'pro': pro})

# Create your views here.

