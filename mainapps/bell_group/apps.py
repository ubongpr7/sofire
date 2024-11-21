from django.apps import AppConfig



class BellGroupConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainapps.bell_group'
    def ready(self):
        import mainapps.bell_group.signals
