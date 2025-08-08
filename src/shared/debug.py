from os import getenv
from typing import Final

DEBUG: Final[bool] = getenv("DEBUG", "False").strip().lower() == "true"