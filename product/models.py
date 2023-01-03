from django.db import models


# Create your models here.


class Product(models.Model):
    
    name = models.CharField(max_length=256,
                                verbose_name='상품명1')
    
    price = models.IntegerField(verbose_name='상품가격')
    
    descrtiption = models.TextField(verbose_name='상품설명')

    stock = models.IntegerField(verbose_name='재고')  
    
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                verbose_name='등록날짜')
    
    
    namecompany = models.CharField(max_length=256,
                                verbose_name='기업명', null=True, default='')
    
    brandcompany = models.CharField(max_length=256,
                                verbose_name='브랜드명', null=True, default='')   
    
    projectcompany = models.CharField(max_length=256,
                                verbose_name='프로젝트명', null=True, default='')    
        
    # numbercompany = models.IntegerField(verbose_name='기업수', null=True, default=0)
    
    # numberbrand = models.IntegerField(verbose_name='브랜드수', null=True, default=0)   
    
    # numberproject = models.IntegerField(verbose_name='프로젝트수', null=True, default=0)    
    
    # numberfake = models.IntegerField(verbose_name='가품수', null=True, default=0)        
        
        
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'lifang_django_product'
        verbose_name = '기업명'
        verbose_name_plural = '기업명'
            
            



# Create your models here.


# class Product(models.Model):
    
#     name = models.CharField(max_length=256,
#                                 verbose_name='상품명')
    
#     price = models.IntegerField(verbose_name='상품가격')
    
#     descrtiption = models.TextField(verbose_name='상품설명')

#     stock = models.IntegerField(verbose_name='재고')  
    
#     registered_dttm = models.DateTimeField(auto_now_add=True,
#                                 verbose_name='등록날짜')
    
    
#     def __str__(self):
#         return self.name
    
#     class Meta:
#         db_table = 'lifang_django_product'
#         verbose_name = '제품'
#         verbose_name_plural = '제품'
            