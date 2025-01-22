# dormmatch/apps.py
from django.apps import AppConfig

class DormmatchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dormmatch'

    def ready(self):
        import dormmatch.signals  # Ensure the signals are imported