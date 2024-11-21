from django.apps import AppConfig



class EventConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainapps.event'
    def ready(self):
        import mainapps.event.signals
