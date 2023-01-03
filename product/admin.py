from django.contrib import admin
from .models import Product
from django.contrib.humanize.templatetags.humanize import intcomma

#태그를 바로 쓰면 안된다. 아래 함수를 쓰면 html로 인식한다.
from django.utils.html import format_html


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_format', 'styled_stock' )
    
    list_filter = ('stock',)
    
    def price_format(self,obj):
      price = intcomma(obj.price)
      return f'{price}원'

    
    
    def styled_stock(self,obj):
        
        stock = obj.stock
        
        if stock <= 50:
            stock = intcomma(stock)
            return format_html(f'<b><span style="color:red">{stock}개</span></b>') 
        return f'{intcomma(stock)}개'
    
    def changelist_view(self, request, extra_context=None):
    # 우리가 원하는 동작
        extra_context = { 'title' : '상품 목록' }
        return super().changelist_view(request, extra_context)
    
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
    # 우리가 원하는 동작
        product = Product.objects.get(pk=object_id)
        
        extra_context = { 'title' : f'{product.name} 수정하기' }
        return super().changeform_view(request, object_id, form_url, extra_context)
        
            
    
    price_format.short_description = '가격'
    styled_stock.short_description = '재고'
admin.site.register(Product, ProductAdmin)