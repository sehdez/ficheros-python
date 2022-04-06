from tabnanny import verbose
from django.apps import AppConfig


class PrimeraAppPruebaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'primera_app_prueba'
    verbose_name = 'Mi primera Aplicación'
