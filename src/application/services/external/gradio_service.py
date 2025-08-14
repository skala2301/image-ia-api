from gradio_client import Client, handle_file
from pydantic import AnyUrl
from typing import Any
from os import getenv
from src.application.dtos import ResponseDataDictDTO

from src.domain.schema.image_edit_payload import ImgExpandPayloadV2
from src.shared.helpers.encode import encode_image_to_base64

import logging # Import logging

# Configure basic logging for debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class GradioService:
    def __init__(self, gradio_url: str) -> None:
        """
        Initialize the GradioService with the provided Gradio URL.
        
        Args:
            gradio_url (str): The URL of the Gradio interface.
        """
        hf_token=getenv("GRADIO_HF_TOKEN")
        if not gradio_url or not hf_token:
            raise ValueError("Gradio URL must be provided.")
        
        self.client = Client(gradio_url, hf_token=hf_token)

    async def outpaint(
            self, 
            img_payload: ImgExpandPayloadV2,
            api_name: str ="/inpaint"
    ) -> dict[str, Any] | None:
        """
        Outpaint an image using the Gradio interface.
        
        Args:
            image (AnyUrl): The URL of the input image to be outpainted.
            width (int): The width of the output image.
            height (int): The height of the output image.
            overlap_percentage (int): The percentage of overlap for the outpainting.
            num_inference_steps (int): The number of inference steps for the model.
            resize_option (str, optional): Resize option for the image. Defaults to "full".
            custom_resize_percentage (int, optional): Custom resize percentage if resize_option is "custom". Defaults to 50.
            prompt_input (str, optional): Text prompt for guiding the outpainting. Defaults to "".
            alignment (str, optional): Alignment option for the outpainting. Defaults to "Middle".
            overlap_left (bool, optional): Whether to apply overlap on the left side. Defaults to True.
            overlap_right (bool, optional): Whether to apply overlap on the right side. Defaults to True.
            overlap_top (bool, optional): Whether to apply overlap on the top side. Defaults to True.
            overlap_bottom (bool, optional): Whether to apply overlap on the bottom side. Defaults to True.
            api_name (str, optional): The API endpoint name for outpainting. Defaults to "/inpaint".
        
        Returns:
            str: Base64 encoded string of the outpainted image.
        """
        logging.info("Starting outpainting process with payload: %s", img_payload)
        # result = img_payload
        try:
            if img_payload.has_url:
                image_data=handle_file(img_payload.url)
            elif img_payload.image:
                if(img_payload.image.url):
                    image_url = img_payload.image.url
                else:
                    image_url = ''
                if(img_payload.image.size):
                    image_size = img_payload.image.size
                else:
                    image_size = None
                if(img_payload.image.mime_type):
                    image_mime_type = img_payload.image.mime_type
                else:
                    image_mime_type = None
                image_data={
                    "path": None,
                    "meta": {"_type": "gradio.FileData"},
                    "orig_name": "None",
                    "url": image_url,
                    "size": image_size,
                    "mime_type": image_mime_type
                }
            result = self.client.predict(
                    image=image_data,
                    width=img_payload.width,
                    height=img_payload.height,
                    overlap_percentage=img_payload.overlap_percentage,
                    num_inference_steps=img_payload.num_inference_steps,
                    resize_option=img_payload.resize_option,
                    custom_resize_percentage=img_payload.custom_resize_percentage,
                    prompt_input=img_payload.prompt,
                    alignment=img_payload.alignment,
                    overlap_left=img_payload.overlap_left,
                    overlap_right=img_payload.overlap_right,
                    overlap_top=img_payload.overlap_top,
                    overlap_bottom=img_payload.overlap_bottom,
                    api_name=api_name
            )

            image_b64=encode_image_to_base64(result[0])
            return ResponseDataDictDTO(
                message="Image outpainted successfully",
                data={"generated_image_b64": image_b64,
                      "success": True}
            )
        except Exception as e:
            logging.error(f"Gradio AI API call or response processing error: {e}", exc_info=True)
            raise RuntimeError(f"Gradio AI API call or image processing failed: {e}")