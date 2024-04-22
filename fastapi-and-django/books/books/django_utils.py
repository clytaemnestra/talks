import os
from django import setup
from django.apps import apps
from books.settings import INSTALLED_APPS

_ALREADY_INITIALIZED_DJANGO = False


def initialize_django():
    global _ALREADY_INITIALIZED_DJANGO
    if not _ALREADY_INITIALIZED_DJANGO:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "books.settings")
        setup()
        apps.populate(INSTALLED_APPS)
        _ALREADY_INITIALIZED_DJANGO = True
