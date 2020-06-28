#-*- coding: utf-8 -*-
from django.apps import AppConfig

class appConfig(AppConfig):
    name = 'app'

    def ready(self):
        from app import updater
        updater.start()
