from pydantic import BaseModel, ConfigDict,Field
from typing import Annotated, Any
from src.domain.constants.examples import TINY_IMAGE_B64, TINY_MASK_IMAGE_B64



google_payload_example: dict[str, Any] = {
    "input_image_b64": TINY_IMAGE_B64, # Use placeholder or truncated actual data
    "mask_image_b64": TINY_MASK_IMAGE_B64,  # Use placeholder or truncated actual data
    "prompt": "A cozy, minimalist living room with a large window overlooking a city skyline. Add some modern art on the walls.",
    "model": "imagen-3.0-capability-001",
    "mask_dilation": 0.03 
}


class GooglePayload(BaseModel):
    """Schema for the payload to outpaint an image using Vertex AI."""

    input_image_b64: Annotated[
        str,
        Field(min_length=1, description="Base64 encoded string of the input reference image."),
    ]
    mask_image_b64: Annotated[
        str,
        Field(min_length=1, description="Base64 encoded string of the mask image (white for active, black for inactive areas)."),
    ]
    prompt: Annotated[
        str,
        Field(description="Text prompt to guide the image generation or editing."),
    ]
    model: Annotated[
        str,
        Field(description="Name of the Vertex AI model to use (e.g., 'imagen-3.0-capability-001')."),
    ]
    mask_dilation: Annotated[
        float,
        Field(default=0.03, description="Mask dilation factor. A float between 0.0 and 1.0 that expands the mask's boundaries. Defaults to 0.03 if not provided.")
    ]

    model_config: ConfigDict = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
        frozen=True,
        json_schema_extra={"example": google_payload_example},
    )