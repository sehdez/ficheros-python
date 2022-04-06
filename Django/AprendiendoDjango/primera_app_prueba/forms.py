from cProfile import label
from socket import fromshare
from turtle import title
from django import forms
from django.core import validators

class FormArticulo(forms.Form):
    title = forms.CharField(
        label='Titulo',
        max_length=50,
        required=True,
        validators=[
            validators.MinLengthValidator(4,'El título es muy pequeño'),
            validators.RegexValidator('^[A-Za-z0-9 ¿?áéíóú]*$','Título invalido')
        ]
    )
    content = forms.CharField(
        label= 'Contenido:',
        widget= forms.Textarea,
        localize= False
    )

    public = forms.TypedChoiceField(
        label= '¿Público?',
        choices=[(1,'Sí'),(0,'No')]
    )
