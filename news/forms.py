from django import forms
from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(label='Заглавие',max_length=150)
    content = forms.CharField(label='Содержание')
    is_published = forms.BooleanField(label='Опубликовано')
    category = forms.ModelChoiceField(queryset=Category.objects.all())