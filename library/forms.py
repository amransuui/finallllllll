from django import forms 
from .models import Category, BookModel

class BrandForm(forms.ModelForm):
    class Meta:
        moodel = Category
        fields = '__all__'
        
class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = '__all__'
        