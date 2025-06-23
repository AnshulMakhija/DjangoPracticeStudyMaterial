from django.apps import AppConfig


class AbstractbaseclassConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AbstractBaseClass'
