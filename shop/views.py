from django.shortcuts import render
# from django.http import HttpResponse
from django.http import JsonResponse

import json
# import datetime
from  .models import *
# Create your views here.


def home(request):
    return render(request, 'home.html')


def mens(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'mens.html', context)


def womens(request):
	femaleproducts = femaleProduct.objects.all()
	context = {'products': femaleproducts}
	return render(request, 'womens.html', context)


def kids(request):
	kidsproducts = kidsProduct.objects.all()
	context = {'products' : kidsproducts}
	return render(request,'kids.html', context)


def view(request):
	maleproduct = Product.objects.all()
	femaleproduct = femaleProduct.objects.all()
	kidsproduct = kidsProduct.objects.all()
	context = {
		"men": maleproduct, "women": femaleproduct, "children": kidsproduct
		}
	
	return render(request, 'view.html', context)


def cart(request):
	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0}

	context = {'items':items, 'order':order}
	return render(request, 'cart.html', context)


def checkout(request):
	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0}

	context = {'items':items, 'order':order}
	return render(request, 'checkout.html', context)


def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

