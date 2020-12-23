"""
Definition of forms.
"""

from django.contrib.auth.models import User
from django import forms
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from django.db import models
from .models import Comment, Blog, Category, Product, Order
from .cart import Cart

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Логин'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text

class BlogForm (forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'posted', 'image',)
        labels = {'title': "Заголовок", 'description': "Краткое описание", 'content': "Содержание", 'posted': "Дата", 'image': "Изображение"}

#class ProductForm (forms.ModelForm):
#    class Meta:
#        model = Catalog
#        fields = ('title', 'description', 'cost', 'posted', 'image',)
#        labels = {'title': "Заголовок", 'description': "Краткое описание", 'content': "Содержание", 'posted': "Дата", 'author': "Автор", 'image': "Изображение"}

class CartAddProductForm(forms.Form): 
    #Эта форма будет использоваться для добавления продуктов в корзину.
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label='Количество')
    #позволяет пользователю выбрать количество между 1-20. Мы используем поле TypedChoiceField с coerce=int для преобразования ввода в целое число.
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    #позволяет указать, следует ли добавлять сумму к любому существующему значению
    #в корзине для данного продукта (False) или если существующее
    #значение должно быть обновлено с заданным значением (True).

class OrderCreateForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ['name', 'email']
        labels = {'name': "Имя", 'email':"Адрес электронной почты"}


