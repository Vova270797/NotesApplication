try:
    from .local_settings import *
except ImportError:
    print("Create local_settings.py file")
    exit(1)

# ALLOWED_HOSTS
if DEBUG:
    ALLOWED_HOSTS = ["*"]
else:
    ALLOWED_HOSTS = ["*"]  # TODO: Change it in production!
