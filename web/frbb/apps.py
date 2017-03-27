from __future__ import unicode_literals

from django.apps import AppConfig


class FrbbConfig(AppConfig):
    name = 'frbb'

    def ready(self):
        import frbb.signals
