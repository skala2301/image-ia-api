import base64
import io
from PIL import Image, ImageDraw # Import ImageDraw for drawing shapes

def create_mask(
    image_b64: str, # Used only to infer original image dimensions
    left_pixels: int,
    right_pixels: int,
    top_pixels: int,
    bottom_pixels: int
) -> str:
    """
    Creates an expanded image canvas filled with white pixels,
    and then draws a black rectangle in the area where the original image
    (inferred from image_b64) would have been, respecting the padding.

    Args:
        image_b64: The input image as a base64-encoded string. Used to infer
                   the original image's dimensions (width, height).
                   The actual content of this image is NOT pasted.
        left_pixels: Number of white pixels to add to the left side.
        right_pixels: Number of white pixels to add to the right side.
        top_pixels: Number of white pixels to add to the top side.
        bottom_pixels: Number of white pixels to add to the bottom side.

    Returns:
        The new image as a base64-encoded string: a white canvas with
        a black rectangle representing the original image's area.
    """
    if not isinstance(image_b64, str):
        raise TypeError("Input image_b64 must be a string.")
    if not all(isinstance(p, int) and p >= 0 for p in [left_pixels, right_pixels, top_pixels, bottom_pixels]):
        raise ValueError("Padding values (left, right, top, bottom) must be non-negative integers.")

    try:
        # 1. Decode the input base64 string to bytes to get original dimensions
        image_bytes = base64.b64decode(image_b64)
        original_image = Image.open(io.BytesIO(image_bytes))
        original_width, original_height = original_image.size
    except Exception as e:
        raise ValueError(f"Could not decode or open image from base64 input to infer dimensions: {e}")

    # 2. Calculate the new canvas dimensions
    new_width = original_width + left_pixels + right_pixels
    new_height = original_height + top_pixels + bottom_pixels

    # Define the background color (white) and rectangle color (black)
    # Use RGBA to handle potential alpha channels for consistency if needed,
    # though for solid white/black, RGB is fine.
    canvas_mode = 'RGB'
    white_color = (255, 255, 255) # White background
    black_color = (0, 0, 0)       # Black rectangle

    # 3. Create a new image (the canvas) filled with white
    new_canvas = Image.new(canvas_mode, (new_width, new_height), white_color)

    # 4. Draw a black rectangle at the position where the original image would be
    draw = ImageDraw.Draw(new_canvas)
    
    # Coordinates for the rectangle: (x_start, y_start, x_end, y_end)
    # x_start = left_pixels
    # y_start = top_pixels
    # x_end = left_pixels + original_width
    # y_end = top_pixels + original_height
    draw.rectangle(
        (left_pixels, top_pixels, left_pixels + original_width, top_pixels + original_height),
        fill=black_color
    )

    # 5. Convert the new PIL Image back to bytes
    output_buffer = io.BytesIO()
    # Save as PNG to avoid compression artifacts that might make solid colors fuzzy
    new_canvas.save(output_buffer, format="PNG") 

    # 6. Encode the bytes to base64 string and return
    return base64.b64encode(output_buffer.getvalue()).decode("utf-8")

