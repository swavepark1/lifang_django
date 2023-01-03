from django.db import models

# Create your models here.


class Lifanguser(models.Model):
    
    email = models.EmailField(max_length=128,
                                verbose_name='사용자 이메일')
    
    password = models.CharField(max_length=128,
                                verbose_name='비밀번호')
    
    level = models.CharField(max_length=64,
                                verbose_name='등급',
        choices={
          ('admin', 'admin'),
          ('user', 'user'),
            
            
        })
    
    
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                verbose_name='등록시간')
    
    def __str__(self):
        return self.email
    
    
    class Meta:
        db_table = 'lifang_django_lifanguser'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
                