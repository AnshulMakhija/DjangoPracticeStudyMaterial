from django.apps import AppConfig


class SignalAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signal_auth'
    
    def ready(self):
        import signal_auth.signals  # Import the signals module to ensure signals are registered
        
