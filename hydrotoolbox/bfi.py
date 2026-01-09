# this is so we have the client with the dlls loaded in
import logging

from hydrotoolbox import client


LOGGER = logging.getLogger(__name__)


# Placeholder for any BFI specific functions that may be needed
def bfi():
    LOGGER.debug("BFI function called.")
