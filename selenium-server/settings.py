import os

IP_SERVER ="localhost"
PORT_HUB = "4444"
DIR_NAME_HUB = "/wd/hub"
PORT_WEB = "8000"
DIR_NAME_WEB="/"

try:
    from local_settings import *  # NOQA
except ImportError:
    pass
