from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product
from django.views.generic.detail import DetailView
from django.db.models import Q


class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['message'] = 'Listado de productos'
        context['products'] = context['product_list']
        print(context)

        return context


class ProductDetailView(DetailView): # id => PK
    model = Product # En la clase de debe indicar el modelo.
    template_name = 'products/product.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)

        print(context)

        return (context)


class ProductSearchListView(ListView):
    template_name = 'products/search.html'

    def get_queryset(self):
        # Para buscar por titulo del producto o titulo de la categoria. 
        filters = Q(title__icontains=self.query()) | Q(category__title__icontains=self.query())
        return Product.objects.filter(filters)

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] = context['product_list'].count()

        return context
