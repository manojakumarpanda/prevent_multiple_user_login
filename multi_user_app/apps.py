from django.apps import AppConfig


class MultiUserAppConfig(AppConfig):
    name = 'multi_user_app'

    def ready(self):
        import multi_user_app.signals
