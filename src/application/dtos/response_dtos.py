from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any


@dataclass
class ResponseBase:
    """Base Response DTO for API or service responses"""

    message: str | None = None
    timestamp: str = field(default_factory=lambda: datetime.now(UTC).isoformat())


@dataclass
class ResponseDataDictDTO(ResponseBase):
    """Generic Response DTO for API or service responses"""

    data: dict[str, Any] | None = field(default=None)


@dataclass
class ResponseDataListDTO(ResponseBase):
    """Generic Response DTO for API or service responses"""

    data: list[Any] | None = field(default=None)