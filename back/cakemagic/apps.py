from django.apps import AppConfig


class CakemagicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cakemagic'

    def ready(self):
        import cakemagic.signals