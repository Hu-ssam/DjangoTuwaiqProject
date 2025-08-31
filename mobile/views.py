from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Category, Products, Cart
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
import requests
# Create your views here.
def welcome(request):
    return HttpResponse("اهلا بكم في دروس جانقو")
def LandPage(request):
    category = Category.objects.all()
    context = {
        'data':category
    }
    return render(request, "landpage.html", context)
    template = loader.get_template('landpage.html')
    return HttpResponse(template.render())
def GetData(request):
    data = {
        'name': 'Hussam',
        'age' : 25,
        'skills': ['Python', 'Django', 'JavaScript']
    }
    return JsonResponse(data)
def datasend(request, name):
    return HttpResponse(name)
def add(request, num1, num2):
    return HttpResponse(num1 + num2)
def runindex(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def aboutus(request):
    template = loader.get_template('aboutus.html')
    return HttpResponse(template.render())
def blog(request):
    template = loader.get_template('blog.html')
    return HttpResponse(template.render())
def invoice(request):
    if request.method == "POST":
        phone_id = request.GET.get("id")
        full_name = request.POST.get("full_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
    phone = [
        {
            "id":"0001",
            "name": "iPhone 15 Pro",
            "brand": "Apple",
            "price": 4599,
            "storage": "256GB",
            "color": "White",
            "image": "images/iphone15.jpg"
        },
        {
            "id":"0002",
            "name": "Galaxy S24 Ultra",
            "brand": "Samsung",
            "price": 3599,
            "storage": "256GB",
            "color": "Black",
            "image": "images/galaxy_s24.jpg"
        },
        {
            "id":"0003",
            "name": "Pixel 8 Pro",
            "brand": "Google",
            "price": 3299,
            "storage": "256GB",
            "color": "Gray",
            "image": "images/pixel8.jpg"
        }
    ]
    phones = [p for p in phone if str(p["id"]) == str(phone_id)]
    return render(request, "invoice.html", {
        "full_name":full_name,
        "phone":phone,
        "email":email,
        "product":phones
    })
def getPhoneMenue(request):
    id = request.GET.get('id')
    product = Products.objects.filter(category_id=id)
    context = {"product": product}
    return render(request, "phonemenue.html", context)
def details(request):
    phone_id = request.GET.get('id')
    product = Products.objects.filter(id=phone_id)
    context = {"product": product}
    return render(request, "details.html",context)
def add_to_cart(request):
    product_id = request.GET.get("id")
    cart_item, created  = Cart.objects.get_or_create(
        product_id = product_id,
        defaults={"quantity":1}
    )
    if not created:
        cart_item.quantity+=1
        cart_item.save()
    product = Products.objects.filter(id=product_id)
    context = {"product": product}
    return render(request, "details.html",context)

@login_required(login_url='login')
def checkout(request):
    cart = Cart.objects.select_related("product").all()
    context = {"cart":cart}
    return render(request,'checkout.html',context)
@csrf_exempt
def auth_login(request):
    template = loader.get_template('auth/auth_login.html')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('checkout')
    return render(request, 'auth/auth_login.html')
@csrf_exempt
def auth_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm(request.POST)
    return render(request, 'auth/auth_register.html', {'form':form})
def get_remote_products(request):
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data, safe=False)
def get_remote_products_view(request):
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    data = {"name": 10, "age":20}
    return render(request, 'remoteproducts.html', {'data':data})