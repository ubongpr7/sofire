from django.contrib import admin


def register_models(models_to_register:list):
    for model in models_to_register:
        admin.site.register(model)