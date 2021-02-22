from django.apps import AppConfig
from django.db.models.signals import post_migrate


class ProfilesConfig(AppConfig):
    name = 'profiles'

    def ready(self):
        import profiles.signals
        from .signals import populate_models
        post_migrate.connect(populate_models, sender=self)

