from enum import StrEnum
from typing import Final

BASE: Final[str] = "/api"


class API(StrEnum):
    """API endpoint constants."""

    V1 = f"{BASE}/v1"

class APIContentType(StrEnum):
    """API content type constants."""

    JSON = "application/json"
    FORM_URLENCODED = "application/x-www-form-urlencoded"
    MULTIPART_FORM_DATA = "multipart/form-data"
    XML = "application/xml"
    TEXT_PLAIN = "text/plain"
    TEXT_HTML = "text/html"
