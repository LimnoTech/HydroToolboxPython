from .log import setup_logger

setup_logger()

# The DLL loader needs to be imported before any of the the modules
# which import the VB/.NET namespaces
from .dll_loader import client

from .bfi import bfi, bfi_from_rdb
