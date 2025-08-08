import base64
import io
from PIL import Image

def add_black_pixel_padding(
    image_b64: str,
    left_pixels: int,
    right_pixels: int,
    top_pixels: int,
    bottom_pixels: int
) -> str:
    """
    Adds black pixels as padding to the sides of a base64-encoded image.

    Args:
        image_b64: The input image as a base64-encoded string.
        left_pixels: Number of black pixels to add to the left side.
        right_pixels: Number of black pixels to add to the right side.
        top_pixels: Number of black pixels to add to the top side.
        bottom_pixels: Number of black pixels to add to the bottom side.

    Returns:
        The new image as a base64-encoded string with the added black padding.
    """
    if not isinstance(image_b64, str):
        raise TypeError("Input image_b64 must be a string.")
    if not all(isinstance(p, int) and p >= 0 for p in [left_pixels, right_pixels, top_pixels, bottom_pixels]):
        raise ValueError("Padding values (left, right, top, bottom) must be non-negative integers.")

    try:
        # 1. Decode the input base64 string to bytes
        image_bytes = base64.b64decode(image_b64)
    except Exception as e:
        raise ValueError(f"Could not decode base64 input image: {e}")

    try:
        # 2. Open the image bytes with PIL
        original_image = Image.open(io.BytesIO(image_bytes))
    except Exception as e:
        raise ValueError(f"Could not open image from bytes. Ensure it's a valid image format: {e}")

    original_width, original_height = original_image.size

    new_width = original_width + left_pixels + right_pixels
    new_height = original_height + top_pixels + bottom_pixels

    # Determine the mode for the new image.
    # If the original has an alpha channel, use RGBA and a black transparent background.
    # Otherwise, use RGB and a solid black background.
    if original_image.mode in ('RGBA', 'LA') or original_image.mode == 'P' and 'transparency' in original_image.info:
        new_mode = 'RGBA'
        background_color = (0, 0, 0, 255) # Solid black with full opacity
        # If the original image was 'P' (palette) mode, convert it to RGBA first for consistent padding
        if original_image.mode == 'P':
            original_image = original_image.convert('RGBA')
    else:
        new_mode = 'RGB'
        background_color = (0, 0, 0) # Solid black

    # 3. Create a new blank image with the desired black background and new dimensions
    new_image = Image.new(new_mode, (new_width, new_height), background_color)

    # 4. Paste the original image onto the new canvas at the correct offset
    new_image.paste(original_image, (left_pixels, top_pixels))

    # 5. Convert the new PIL Image back to bytes
    output_buffer = io.BytesIO()
    # Save as PNG to preserve alpha channel if present, otherwise JPEG is fine but PNG is safer.
    # If the original was JPEG and you explicitly need JPEG output, handle mode conversion carefully.
    save_format = "PNG" if new_mode == "RGBA" else "JPEG"
    try:
        new_image.save(output_buffer, format=save_format)
    except Exception as e:
        raise RuntimeError(f"Failed to save padded image to buffer in {save_format} format: {e}")

    # 6. Encode the bytes to base64 string and return
    return base64.b64encode(output_buffer.getvalue()).decode("utf-8")

