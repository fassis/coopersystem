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
from datetime import datetime
from core.forms import OrderEditForm, OrderForm, ProductForm, ProductUpdateForm

from core.models import ENTREGUE, ENVIADO, PENDENTE, Product, Order

def login_api(request):
	return render(request, 'login_api.html')

@login_required
def index(request):
	return render(request, 'base.html')

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
@csrf_exempt
def product_create(request):
    form = ProductForm( request.POST or None)
    if request.method =="POST":
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
    if request.method =="POST":
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

@login_required
@csrf_exempt
def product_delete(request,pk):
    object = get_object_or_404(Product,pk=pk)
    form = ProductUpdateForm( request.POST or None, instance=object)
    if request.method =="POST":
        object.delete()
        messages.add_message(request, messages.SUCCESS,
                            'Produto Deletado com sucesso.')
        return HttpResponseRedirect(reverse_lazy('product_list'))
    else:
        context = {
                    'form':form,
                    'action':'/product_delete/%d/'%(pk),
                    'title':'Produtos',
                    }
    return render(request, 'product_list.html', context)

@login_required
@csrf_exempt
def order_create(request,product_pk):
    product = get_object_or_404(Product,pk=product_pk)
    form = OrderForm(product, request.POST or None, initial={'product':product})
    if request.method =="POST":
        if form.is_valid():
            order = form.save(commit=False)
            order.value = product.value*order.quantity
            order.save()
            product.quantity -= order.quantity
            product.save()
            messages.add_message(request, messages.SUCCESS,
                                'Pedido criado com sucesso.')
            return HttpResponseRedirect(reverse_lazy('order_list'))
    
    if product.quantity > 0:
            messages.add_message(request, messages.INFO,
                            'Atenção! Somente %d itens disponíveis!'%(product.quantity))
    else:
        messages.add_message(request, messages.ERROR,
                            'Produto indisponível no momento!')
    context = {
                'form':form,
                'action':'/order_create/%d/'%(product_pk),
                'title':'Pedidos',
                }
    return render(request, 'order_list.html', context)

@login_required
def order_detail(request,pk):
    order = get_object_or_404(Order,pk=pk)
    context = {
                'order':order,
                'action':'/product_delete/%d/'%(pk),
                'title':'Detalhes do Pedido %d'%(pk),
                }
    return render(request, 'order_detail.html', context)

@login_required
@csrf_exempt
def order_update(request,pk):
    order = get_object_or_404(Order,pk=pk)
    product = get_object_or_404(Product,pk=order.product.pk)
    form = OrderEditForm(request.POST or None,instance=order)
    if request.method =="POST" and order.situation == PENDENTE:
        before_quantity = order.quantity
        if form.is_valid():
            order = form.save(commit=False)
            order.value = product.value*order.quantity
            order.save()
            if order.quantity > before_quantity:
                product.quantity -= (order.quantity-before_quantity)
            else:
                product.quantity += (before_quantity - order.quantity)
            product.save()
            messages.add_message(request, messages.SUCCESS,
                                'Pedido editado com sucesso.')
            return HttpResponseRedirect(reverse_lazy('order_list'))
    
    if product.quantity > 0:
            messages.add_message(request, messages.INFO,
                            'Atenção! Somente %d itens disponíveis!'%(product.quantity))
    else:
        messages.add_message(request, messages.ERROR,
                            'Produto indisponível no momento!')
    if order.situation > PENDENTE:
        messages.add_message(request, messages.ERROR,
                            'Não é possível editar pedidos enviados ou recebidos!')
    context = {
                'form':form,
                'action':'/order_update/%d/'%(pk),
                'title':'Pedidos',
                }
    return render(request, 'order_list.html', context)

@login_required
def order_list(request):

    orders = Order.objects.all().order_by('-created_at')

    context = {
        'object_list': orders,
        'title':'Pedidos',
        'action':'/order_create/'
        }
    
    #return HttpResponse(orders)

    return render(request, 'order_list.html', context)

@login_required
@csrf_exempt
def order_delete(request,pk):
    order = get_object_or_404(Order,pk=pk)
    if request.method =="POST" and order.situation == PENDENTE:
        product = order.product
        product.quantity += order.quantity
        product.save()
        order.delete()
        messages.add_message(request, messages.SUCCESS,
                            'Pedido deletado com sucesso. Produtos voltaram ao estoque')
        return HttpResponseRedirect(reverse_lazy('order_list'))
    else:
        if order.situation > PENDENTE:
            messages.add_message(request, messages.ERROR,
                            'Não é possível excluir pedidos enviados ou recebidos!')
        context = {
                    'action':'/order_delete/%d/'%(pk),
                    'title':'Pedidos',
                    }
    return render(request, 'order_list.html', context)


@login_required
@csrf_exempt
def order_send(request,pk):
    order = get_object_or_404(Order,pk=pk)
    if request.method =="POST" and order.situation == PENDENTE:
        order.situation = ENVIADO
        order.sent_at = datetime.now()
        order.save()
        messages.add_message(request, messages.SUCCESS,
                            'Pedido enviado com sucesso!')
        return HttpResponseRedirect(reverse_lazy('order_list'))
    else:
        if order.situation > PENDENTE:
            messages.add_message(request, messages.ERROR,
                            'Pedido já foi enviado ou recebido!')
        context = {
                    'title':'Pedidos',
                    }
    return render(request, 'order_list.html', context)


@login_required
@csrf_exempt
def order_delivered(request,pk):
    order = get_object_or_404(Order,pk=pk)
    if request.method =="POST" and order.situation == ENVIADO:
        order.situation = ENTREGUE
        order.received_at = datetime.now()
        order.save()
        messages.add_message(request, messages.SUCCESS,
                            'Pedido entregue com sucesso!')
        return HttpResponseRedirect(reverse_lazy('order_list'))
    else:
        if order.situation > ENVIADO:
            messages.add_message(request, messages.ERROR,
                            'Pedido já foi enviado ou recebido!')
        context = {
                    'title':'Pedidos',
                    }
    return render(request, 'order_list.html', context)