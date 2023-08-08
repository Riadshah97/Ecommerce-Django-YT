from django.db.models import Count
from django.shortcuts import render
from django.views import View
from .models import Product


# Create your views here.

def home(request):
    return render(request, "home.html")

#def category(request):
   # return render(request, 'category.html')

class Categoryview(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        titles = Product.objects.filter(category=val).values('title')
        return render(request, "category.html", locals())

class ProductDetails(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request, "productdetail.html", locals())


