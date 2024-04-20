_ALREADY_INITIALIZED_DJANGO = False


def with_django_initialized(func):
    import functools

    @functools.wraps(func)
    def _initialize_django_before_execution(*args, **kwargs):
        initialize_django_and_logging()
        return func(*args, **kwargs)

    return _initialize_django_before_execution


def initialize_django_and_logging():
    """Makes sure that Django is initialized only one time"""
    global _ALREADY_INITIALIZED_DJANGO
    if _ALREADY_INITIALIZED_DJANGO is False:
        from os import environ

        from django import setup

        environ.setdefault("DJANGO_SETTINGS_MODULE", "books.settings")
        setup()

        _ALREADY_INITIALIZED_DJANGO = True
