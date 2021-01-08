from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from django.db.models import Q
from .models import *
from blog.models import *
import random
from django.core.paginator import Paginator


def store (request):
    products = Product.objects.all().order_by('-date')
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    context ={'products':products}
    return render (request,'store/store.html',context)
    

def product(request,id):

    product = Product.objects.get(pk=id)
   
    # Add review
    related_products = list(Product.objects.filter(category=product.category).exclude(id=product.id))
    
    if len(related_products) >= 3:
        related_products = random.sample(related_products, 3)

    imagesstring = "{'image': '%s'}," % ( product.image.url)
    category_products= list(Product.objects.filter(category=product.category))
    imagesstring = "{'image': '%s'}," % ( product.image.url)
    context= {'product':product,
              'related_products':related_products,
              'category_products':category_products}
    return render(request, "store/product.html", context)
    product.save()


def productreview(request,id):
        product = Product.objects.get(pk=id)
        related_products = list(Product.objects.filter(category=product.category).exclude(id=product.id))
    
        if len(related_products) >= 3:
            related_products = random.sample(related_products, 3)

        imagesstring = "{'image': '%s'}," % ( product.image.url)
        context= {'product':product,
                   'related_products':related_products}
        stars = request.POST.get('stars', 3)
        content = request.POST.get('content', '')
        date_added= request.POST.get('date_added', '')
        review = ProductReview.objects.create(product=product, stars=stars, content=content,date_added=date_added)
        return render(request, "store/product.html", context)
        review.save()
        return redirect('product')


def Category (request):
    products = Product.objects.all
    category_products= list(Product.objects.filter(category=request.POST.get('Category')))
    #imagesstring = "{'image': '%s'}," % ( product.image.url)
    context= {'product':product,
              'category_products':category_products}
    return render (request,'store/store.html',context)

