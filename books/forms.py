from django import forms
from django.db.models import fields
from .models import Books


class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'
