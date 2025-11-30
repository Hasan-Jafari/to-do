DJANGO_SETTINGS_MODULE = 'config.settings.dev'



if DJANGO_SETTINGS_MODULE == 'config.settings.dev':
    from .dev import *
elif DJANGO_SETTINGS_MODULE == 'config.settings.pro':
    from .pro import *
else:
    from .dev import *