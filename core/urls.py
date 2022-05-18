from django.urls import path
from . import views, api_views

urlpatterns = [

	### Login ###
	path('api/register/', 
		api_views.RegisterAPI.as_view(), 
		name='register'),
	
	### API VIEWS ###
    
	path('urls', api_views.api_overview, 
		name="api-overview"),
	path('product-list/', 
		api_views.api_product_list, 
		name="product-list"),
	path('product-detail/<str:pk>/', 
		api_views.api_product_detail, 
		name="product-detail"),
	path('product-create/', 
		api_views.api_product_create, 
		name="product-create"),

	path('product-update/<str:pk>/', 
		api_views.api_product_update, 
		name="product-update"),
	path('product-delete/<str:pk>/', 
		api_views.api_product_delete, 
		name="product-delete"),

	### VIEWS ###

	path('', views.index, name="index"),
	
	path('product_list/', 
        views.product_list, 
		name='product_list'),
	
	path('product_create/', 
        views.product_create, 
		name='product_create'),
	
	path('product_update/<int:pk>/', 
        views.product_update, 
		name='product_update'),
	
	path('product_delete/<int:pk>/', 
        views.product_delete, 
		name='product_delete'),
	
	path('order_list/', 
        views.order_list, 
        name='order_list'),
	
	path('order_create/<int:product_pk>/',
        views.order_create,
		name='order_create'),

	path('order_update/<int:order_pk>/',
        views.order_update,
		name='order_update'),
	
	path('order_delete/<int:pk>/', 
        views.order_delete, 
		name='order_delete'),
	
	path('order_send/<int:pk>/', 
        views.order_send, 
		name='order_send'),
	
	path('order_delivered/<int:pk>/', 
        views.order_delivered, 
		name='order_delivered'),
	
]