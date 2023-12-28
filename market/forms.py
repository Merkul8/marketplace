from django import forms
from .models import Product, ProductImage
from django.utils.text import slugify

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'price', 'product_count', 'categories']
        widgets = {
            'name': forms.TextInput(attrs={"rows": 1, 'class': 'form-control'}),
            'price': forms.TextInput(attrs={"rows": 1, 'class': 'form-control'}),
            'product_count': forms.TextInput(attrs={"rows": 1, 'class': 'form-control'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = slugify(instance.name)
        if commit:
            instance.save()
            self.save_m2m()
        return instance

class ProductImageForm(forms.ModelForm):
   class Meta:
       model = ProductImage
       fields = ['image']
       widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control', 'type': 'file'}),
        }

