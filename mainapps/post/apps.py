from django.apps import AppConfig



class PostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainapps.post'
    def ready(self):
        import mainapps.post.signals
