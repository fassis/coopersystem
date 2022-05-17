import json
from multiprocessing import context
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.contrib import messages
from rest_framework.renderers import JSONRenderer
from core.forms import ProductForm

from core.models import Product, Order

@login_required
def product_list(request):
    products = Product.objects.all().order_by('-created_at')
	
	form = ProductForm()
	context = {'object_list': products,
				'title':'Produtos',
				'form':form,
				}

    return render(request, 'generic_list.html', context )


@login_required
def order_list(request):
    orders = Order.objects.all().order_by('-created_at')
    
	context = {'object_list': orders,'title':'Pedidos'}

    return render(request, 'generic_list.html', context)