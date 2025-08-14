import base64

def encode_image_to_base64(filepath):
    """Encodes an image file to a base64 string."""
    with open(filepath, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

