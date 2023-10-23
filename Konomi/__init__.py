from typing import List
from requests import get
from colorama import Fore, Style

__title__ = 'Konomi'
__author__ = 'Kono'
__license__ = 'MIT'
__copyright__ = 'Kono 2023 Copyright'
__version__ = '0.0.0.0'
__description__ = 'Secret sauce to use on app with letter (a)'

from .bot import Bot
from .async_bot import AsyncBot
from .client import Client
from .async_client import AsyncClient

__all__: List[str] = [
    'Bot',
    'AsyncBot',
    'Client',
    'AsyncClient',]

print("Project Arsenal.")

