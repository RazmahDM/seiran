from django.db import models



class Field(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'

class Category(models.Model):
    img = models.ImageField('Картинка')
    title = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
class Product(models.Model):
    img = models.ImageField('Картинка')
    title = models.CharField(max_length=255, verbose_name='Название')
    price = models.IntegerField(max_length=255, verbose_name='Цена')
    fields = models.ManyToManyField(Field, verbose_name='Характеристики')
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING, verbose_name='Категория')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    
    