from django import forms
from django.core import validators

class FormArticle(forms.Form):

    title = forms.CharField(
        label= "Titulo:",
        max_length= 20,
        required=True,
        validators =[
            validators.MinLengthValidator(4,'El texto es muy corto.'),
            validators.RegexValidator('^[A-Za-z0-9 ?áéíóú]*$', 'El titulo está mal formado','invalid_title')
        ]

    )
    content = forms.CharField(
        label= "Contenido:",
        widget=forms.Textarea
    )

    public_options =[(1,'Sí'),(0,'No')]

    public = forms.TypedChoiceField (
        label= "¿Publico?",
        choices = public_options
    )
    