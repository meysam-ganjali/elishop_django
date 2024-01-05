from django.db import models

class CustomerUser(models.Model):
    name = models.CharField(max_length=60,verbose_name='نام و نام خانوادگی')
    is_active = models.BooleanField(default=False,verbose_name='فعال/غیرفعال')
    phone_number = models.CharField(max_length=11,verbose_name='شماره موبایل')
    password=models.CharField(max_length=15,verbose_name='کلمه عبور')
    def __str__(self):
        return  f'{self.name} - {self.phone_number}'
    class Meta:
        verbose_name='مدیریت مشتری'
        verbose_name_plural='مدیریت مشتریان'


class UserAddress(models.Model):
    address = models.TextField(verbose_name='آدرس')
    customerUser = models.ForeignKey(to=CustomerUser,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.address}'
    class Meta:
        verbose_name='مدیریت آدرس'
        verbose_name_plural='مدیریت آدرس ها'


