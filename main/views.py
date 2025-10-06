import datetime
from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product
from main.forms import ProductForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Show main page
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "my":
        product_list = Product.objects.filter(user=request.user)
    elif filter_type == "featured":
        product_list = Product.objects.filter(is_featured=True)
    else:
        product_list = Product.objects.all()

    context = {
        'npm' : '2406406300',
        'name': request.user.username,
        'user': request.user,
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

# Show product registration page (login required)
@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        registered_product = form.save(commit=False)
        registered_product.user = request.user
        registered_product.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "create_product.html", context)

# Show product detail page for given id
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

# Show product edit page
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')
    
    context = {
        'form': form,
        'thumbnail': product.thumbnail
    }

    return render(request, "edit_product.html", context)

# Delete a product (no page)
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

# Show user registration page
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account creation successful!\nPlease log in using your new credentials.")
            return redirect('main:login')
        
    context = {'form':form}
    return render(request, 'register.html', context)

# Show user login page
def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    
    else:
        form = AuthenticationForm(request)
    
    context = {'form':form}
    return render(request, 'login.html', context)

# Log out user (no page)
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:show_main'))
    response.delete_cookie('last_login')
    return response

# Show XML data delivery page
def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

# Show JSON data delivery page
def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'stock': product.stock,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'user': product.user_id,
            'username': product.user.username
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

# Show XML data delivery page of specific item
def show_xml_by_id(request, product_id):
    try:
        current_product = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", current_product)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

# Show JSON data delivery page of specific item
def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'stock': product.stock,
            'price': product.price,
            'category': product.category,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'user': product.user_id,
            'username': product.user.username
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail':'Not found'}, status=404)

# Add new product data via AJAX
@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = request.POST.get("title")
    stock = request.POST.get("stock")
    price = request.POST.get("price")
    category = request.POST.get("category")
    description = request.POST.get("content")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == "on"
    user = request.user

    newProduct = Product(
        name = name,
        stock = stock,
        price = price,
        category = category,
        description = description,
        thumbnail = thumbnail,
        is_featured = is_featured,
        user = user
    )
    newProduct.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
def edit_product_ajax(request, product_id):
    edited_data = {
        'name': request.POST.get("etitle"),
        'stock': request.POST.get("estock"),
        'price': request.POST.get("eprice"),
        'category': request.POST.get("ecategory"),
        'description': request.POST.get("econtent"),
        'thumbnail': request.POST.get("ethumbnail"),
        'is_featured': request.POST.get("eis_featured") == "on",
        'user': request.user
    }

    Product.objects.filter(pk=product_id).update(**edited_data)

    return HttpResponse(b"EDITED", status=201)

@csrf_exempt
@require_POST
def login_ajax(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    if user != None:
        login(request, user)
        return JsonResponse({
            'status': 'success',
            'message': 'Login successful!'
        })
    else:
        return JsonResponse({
            'status': 'error',
            'message': 'Incorrect username or password!'
        }, status=401)
    
@csrf_exempt
@require_POST
def register_ajax(request):
    print("Perform AJAX View")

    username = request.POST.get('username')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')

    if not username or not password1 or not password2:
        return JsonResponse({
            'status': 'error',
            'message': 'Please fill in all fields.'
        }, status=400)
    
    if password1 != password2:
        return JsonResponse({
            'status': 'error',
            'message': 'Passwords do not match.'
        }, status=400)
    
    if User.objects.filter(username=username).exists():
        return JsonResponse({
            'status': 'error',
            'message': 'Username already exists. Please choose a different username.'
        }, status=400)
    
    user = User.objects.create_user(username=username, password=password1)
    login(request, user)

    return JsonResponse({
            'status': 'success',
            'message': 'Registration successful!'
        })