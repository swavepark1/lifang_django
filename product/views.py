from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Product
from django.utils.decorators import method_decorator
from rest_framework import generics
from rest_framework import mixins

from lifanguser.decorator import login_requierd, admin_requierd
from .forms import RegisterForm 
from .serializer import ProdectSerializer

from order.forms import RegisterForm as OrderForm 

# Create your views here.

#레스트 프레임워크
class ProductListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ProdectSerializer
    
    def get_queryset(self):
        return Product.objects.all().order_by('id')
    
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    
#레스트 프레임워크
class ProductDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = ProdectSerializer
    
    def get_queryset(self):
        return Product.objects.all().order_by('id')
    
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    

class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'

@method_decorator(admin_requierd, name='dispatch')
class ProductCreate(FormView):
    model = Product
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'
    

class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data( **kwargs)
        context['form'] = OrderForm(self.request)
        return context