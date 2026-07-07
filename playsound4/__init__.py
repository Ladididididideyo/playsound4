__license__ = "MIT"
__version__ = "4.0.0"
__author__ = "Ogr1sh"

from playsound4.playsound4 import (
    AVAILABLE_BACKENDS,
    DEFAULT_BACKEND,
    PlaysoundException,
    playsound,
    prefer_backends,
)

__all__ = [
    "AVAILABLE_BACKENDS",
    "DEFAULT_BACKEND",
    "playsound",
    "prefer_backends",
    "PlaysoundException",
]
