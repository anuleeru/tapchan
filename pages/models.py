from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Tapchan(models.Model):
    name = models.CharField(max_length=255, verbose_name='Тапчан')
    image = models.ImageField(upload_to="media/", blank=True, null=True)
    price = models.CharField(max_length=255, verbose_name='Цена')
    def __str__(self):
        return self.name  
    
    class Meta:
        verbose_name = "Тапчан"
        verbose_name_plural = "Тапчан"


class Menu(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование блюда')
    image = models.ImageField(upload_to="media/", blank=True, null=True)
    price = models.CharField(max_length=255, verbose_name='Цена', blank=True, null=True)
    
    def __str__(self):
        try:
            return self.name 
        except:
            return self.name  
    
    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"
        

class Order(models.Model):
    name = models.CharField(max_length=255, verbose_name='Заказ')
    tapchan = models.CharField(max_length=255, verbose_name='Тапчан №')
    food = models.TextField(max_length=255, verbose_name='Заказ из меню')
    price = models.CharField(max_length=255, verbose_name='Сумма заказа')
    person = models.CharField(max_length=255, verbose_name='Клиент')
    number = models.CharField(max_length=255, verbose_name='Номер телефона')
    date_rec = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        try:
            return self.name 
        except:
            return self.name  
    
    class Meta:
        verbose_name = "Брони"
        verbose_name_plural = "Брони"



        
        
















    

     

        

# Создать модель для записей
# Поля: Дата записи, имя пользователя, вид услуги, выбор мастера