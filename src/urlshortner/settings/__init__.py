# base.py will always be there
from .base import *

# # if production.py is present, overwrite the base.py
# from .production import *

# # if local.py is present, overwrite the production.py
# try:
#     from .local import *
# except:
#     pass