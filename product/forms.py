from django import forms 
from .models import Product

class RegisterForm(forms.Form):
    name = forms.CharField(
        error_messages={'required' : '상품명을 입력해주세요.'},
        max_length=64, label="상품명")
    
    namecompany = forms.CharField(
        error_messages={'required' : '브랜드명을 입력해주세요.'},
        max_length=64, label="브랜드명")  
    
    brandcompany = forms.CharField(
        error_messages={'required' : '브랜드명을 입력해주세요.'},
        max_length=64, label="기업명")     
    
    projectcompany = forms.CharField(
        error_messages={'required' : '프로젝트명을 입력해주세요.'},
        max_length=64, label="프로젝트명")
    
    # numbercompany = forms.IntegerField(error_messages={'required' : '기업명을 입력해주세요.'},
    #                            label="기업명")       
    
    # numberbrand = forms.IntegerField(error_messages={'required' : '브랜드명을 입력해주세요.'},
    #                            label="브랜드")       

    # numberproject = forms.IntegerField(error_messages={'required' : '프로젝트명을 입력해주세요.'},
    #                            label="프로젝트")       

    # numberfake = forms.IntegerField(error_messages={'required' : '가품명을 입력해주세요.'},
    #                            label="가품")       
    
    price = forms.IntegerField(error_messages={'required' : '상품가격을 입력해주세요.'},
                               label="상품가격")
    
    decription = forms.CharField(error_messages={'required' : '상품명을 입력해주세요'},
                               label="상품설명")
    
    stock = forms.IntegerField(error_messages={'required' : '재고를 입력해주세요.'},
                               label="재고")
    
    
    
    def clean(self):
        cleaned_data = super().clean()
        namecompany = cleaned_data.get('namecompany')
        brandcompany = cleaned_data.get('brandcompany')
        projectcompany = cleaned_data.get('projectcompany')
        # numbercompany = cleaned_data.get('numbercompany')
        # numberbrand = cleaned_data.get('numberbrand')
        # numberproject = cleaned_data.get('numberproject')
        # numberfake = cleaned_data.get('numberfake')
        price = cleaned_data.get('price')
        decription = cleaned_data.get('decription')
        stock = cleaned_data.get('stock')
        
        
        
        if name and price and decription and stock:
            
            product=Product(
                name=name,
                price=price,
                decription=decription,
                stock=stock,
                namecompany=namecompany,
                brandcompany=brandcompany,
                projectcompany=projectcompany,
                # numbercompany=numbercompany,
                # numberbrand=numberbrand,
                # numberproject=numberproject,
                # numberfake=numberfake,
                
            )
            product.save()