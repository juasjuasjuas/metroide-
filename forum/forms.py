from django import forms
from .models import *

class UserPostForm(forms.ModelForm):

    title = forms.CharField(label="", widget=forms.TextInput(attrs={
        'class':'form-control form-control-style-3',
        'placeholder':'Título',
    }))

    description = forms.CharField(label="", widget=forms.Textarea(attrs={
        'class':'form-control form-control-style-3',
        'placeholder':'Describe a detalle...',
        'rows':'8',
        'cols':'80',
    }))

    class Meta:
        model = UserPost
        fields = ['title', 'description']

class AnswerForm(forms.ModelForm):

    content = forms.CharField(label="", widget=forms.Textarea(attrs={
        'class':'form-control form-control-style-3',
        'placeholder':'Escribe tu respuesta...',
        'rows':'8',
        'cols':'50',
    }))

    class Meta:
        model = Answer
        fields = ['content',]