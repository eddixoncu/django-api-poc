from django.apps import AppConfig

# app configuration (misleading filename)

class PlaygroundConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'playground'
