from pydantic import BaseModel, ConfigDict,Field
from typing import Annotated, Any
from src.domain.constants.examples import TINY_IMAGE_B64, TINY_MASK_IMAGE_B64

img_payload_example: dict[str, Any] = {
    "url": TINY_IMAGE_B64,  # Use placeholder or truncated actual data
    "size": None,
    "mime_type": "image/png",
    "orig_name": None,
    "is_stream": False,
}

imgexpand_payload_example: dict[str, Any] = {
    "input_image_b64": TINY_IMAGE_B64, # Use placeholder or truncated actual data
    "prompt": "A cozy, minimalist living room with a large window overlooking a city skyline. Add some modern art on the walls.",
    "mask_dilation": 0.03,
    "left_pixels": 200,
    "right_pixels": 200,
    "top_pixels": 0,
    "bottom_pixels": 0,
}

imgexpand_payload_example_v2: dict[str, Any] = {
    "url": "",  # Use placeholder or truncated actual data
    "has_url": True,
    "image": None,
    "width": 1024,
    "height": 720,
    "overlap_percentage": 10,
    "num_inference_steps": 28,
    "resize_option": "75%",
    "custom_resize_percentage": 50,
    "prompt": "",
    "alignment": "Middle",
    "overlap_left": True,
    "overlap_right": True,
    "overlap_top": True,
    "overlap_bottom": True,
}




class ImgPayload(BaseModel):
    """
    Schema for the payload to expand an image's canvas by adding pixels to its sides.
    This can be used in conjunction with image generation/outpainting.
    """
    url: Annotated[
        str,
        Field(min_length=1, description="Base64 encoded string of the input reference image to be expanded."),
    ]
    size: Annotated[
        int | None,
        Field(default=None, description="Size of the image. If None, the original size is used."),
    ]
    mime_type: Annotated[
        str,
        Field(default="image/png", description="MIME type of the image."),
    ]
    orig_name: Annotated[
        str | None,
        Field(default=None, description="Original name of the image file."),
    ]
    is_stream: Annotated[
        bool,
        Field(default=False, description="Whether the image is a stream or not."),
    ]
    model_config: ConfigDict = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
        frozen=True,
        json_schema_extra={"example": img_payload_example},
    )

class ImgExpandPayload(BaseModel):
    """
    Schema for the payload to expand an image's canvas by adding pixels to its sides.
    This can be used in conjunction with image generation/outpainting.
    """

    input_image_b64: Annotated[
        str,
        Field(min_length=1, description="Base64 encoded string of the input reference image to be expanded."),
    ]
    prompt: Annotated[
        str,
        Field(description="Text prompt to guide the image generation or editing process after expansion."),
    ]
    mask_dilation: Annotated[
        float,
        Field(default=0.03, description="Mask dilation factor. A float between 0.0 and 1.0 that expands the mask's boundaries. Defaults to 0.03 if not provided.")
    ]
    left_pixels: Annotated[
        int,
        Field(default=0, description="Number of pixels to add to the left side of the image canvas.")
    ]
    right_pixels: Annotated[
        int,
        Field(default=0, description="Number of pixels to add to the right side of the image canvas.")
    ]
    top_pixels: Annotated[
        int,
        Field(default=0, description="Number of pixels to add to the top side of the image canvas.")
    ]
    bottom_pixels: Annotated[
        int,
        Field(default=0, description="Number of pixels to add to the bottom side of the image canvas.")
    ]

    model_config: ConfigDict = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
        frozen=True,
        json_schema_extra={"example": imgexpand_payload_example},
    )

class ImgExpandPayloadV2(BaseModel):
    """
    Schema for the payload to expand an image's canvas by adding pixels to its sides.
    This can be used in conjunction with image generation/outpainting.
    """
    print("INTO...")
    url: Annotated[
        str | None,
        Field(description="Base64 encoded string of the input reference image to be expanded."),
    ]
    has_url: Annotated[
        bool,
        Field(default=True, description="Set value as true if the url is provided, otherwise false."),
    ]
    image: ImgPayload | None = None
    width: Annotated[
        int, 
        Field(description="Specifies the output Width."),
    ]
    height: Annotated[
        int, 
        Field( description="Specifies output Height."),
    ]
    overlap_percentage: Annotated[
        int, 
        Field( description="The 'Mask overlap (%)'."),
    ]
    num_inference_steps: Annotated[
        int, 
        Field(description="If is greater it provides better results, but more processing is required."),
    ]
    resize_option: Annotated[
        str | None,
        Field(
            default="Full",
            description="Resize option for the image. Options are Literal['Full', '75%', '50%', '33%', '25%', 'Custom']."
        ),
    ]
    custom_resize_percentage: Annotated[
        int | None, 
        Field(description="If is greater it provides better results, but more processing is required."),
    ]
    prompt: Annotated[
        str, 
        Field(description= "Text prompt to guide the image generation or editing process after expansion.")
    ]
    alignment: Annotated[
        str,
        Field(default="Middle", description="Alignment option for the outpainting. Defaults to 'Middle'."),
    ]
    overlap_left: Annotated[
        bool,
        Field(default=True, description="Alignment option for the outpainting. Defaults to 'Middle'."),
    ]
    overlap_right: Annotated[
        bool,
        Field(default=True, description="Alignment option for the outpainting. Defaults to 'Middle'."),
    ]
    overlap_top: Annotated[
        bool,
        Field(default=True, description="Alignment option for the outpainting. Defaults to 'Middle'."),
    ]
    overlap_bottom: Annotated[
        bool,
        Field(default=True, description="Alignment option for the outpainting. Defaults to 'Middle'."),
    ]

    model_config: ConfigDict = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
        frozen=True,
        json_schema_extra={"example": imgexpand_payload_example_v2},
    )