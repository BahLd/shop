from django import forms
from django.db import models
from django.forms import fields

from .models import Product


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'