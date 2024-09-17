from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'testdjango'

    def ready(self):
        import testdjango.signals