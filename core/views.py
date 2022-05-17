import json
from multiprocessing import context
from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.contrib import messages
from rest_framework.renderers import JSONRenderer
from core.forms import OrderForm, ProductForm, ProductUpdateForm

from core.models import Product, Order

@login_required
def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    
    form = ProductForm()
    context = {'object_list': products,
                'title':'Produtos',
                'form':form,
                'action':'/product_create/'
                }
    return render(request, 'product_list.html', context )


@login_required
def order_list(request):
    orders = Order.objects.all().order_by('-created_at')
    
    form = OrderForm()
    context = {'object_list': orders,
        'title':'Pedidos',
        'form':form,
        'action':'/order_create/'
        }

    return render(request, 'order_list.html', context)

@login_required
@csrf_exempt
def product_create(request):
    form = ProductForm( request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS,
                            'Produto criado com sucesso.')
        return HttpResponseRedirect(reverse_lazy('product_list'))
    else:
        context = {
                    'form':form,
                    'action':'/product_create/',
                    'title':'Produtos',
                    }
    return render(request, 'product_list.html', context)

@login_required
@csrf_exempt
def product_update(request,pk):
    object = get_object_or_404(Product,pk=pk)
    form = ProductUpdateForm( request.POST or None, instance=object)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS,
                            'Produto editado com sucesso.')
        return HttpResponseRedirect(reverse_lazy('product_list'))
    else:
        context = {
                    'form':form,
                    'action':'/product_update/%d/'%(pk),
                    'title':'Produtos',
                    }
    return render(request, 'product_list.html', context)