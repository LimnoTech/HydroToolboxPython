"""This file loads required DLLS for the wrapper and adds them to the CLR client"""

import clr as client
import os

import logging

LOGGER = logging.getLogger(__name__)


def load_dlls(dll_directory: str):
    """Load all DLLs from the specified directory into the CLR client.

    Args:
        dll_directory (str): The directory containing the DLL files.
    """
    for filename in os.listdir(dll_directory):
        if filename.endswith(".dll"):
            dll_path = os.path.join(dll_directory, filename)
            client.AddReference(dll_path)
            LOGGER.debug(f"Loaded DLL: {dll_path}")

            # confirm the dll is now in the namespace
            LOGGER.debug(
                f"Found in client namespaces: {filename[:-4] in client._available_namespaces}"
            )


load_dlls(os.path.dirname(__file__) + "/resources")
