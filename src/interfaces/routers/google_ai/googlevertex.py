from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException

from src.application.dtos.response_dtos import ResponseDataDictDTO
from src.domain.schema.google_payload import GooglePayload
from src.domain.schema.image_edit_payload import ImgExpandPayload
from src.shared.helpers.add_black_pixels import add_black_pixel_padding
from src.shared.helpers.add_mask import create_mask
from src.application.services.external import GoogleService



def getGoogleService() -> GoogleService:
    """Dependency to get the GoogleService instance."""
    return GoogleService()


google_router: APIRouter = APIRouter(
    prefix="/vertex",
    tags=["Vertex"],
    responses={404: {"description": "Not found"}},
)

@google_router.post(
    path="/outpaint",
    summary="Outline an image using Vertex AI",
    response_model=ResponseDataDictDTO,
)
async def outpaint_image(
    payload: ImgExpandPayload,
    google_service: GoogleService = Depends(getGoogleService),
) -> ResponseDataDictDTO:
    """Endpoint to outline an image using Vertex AI."""
    data: GooglePayload = GooglePayload(
        input_image_b64=add_black_pixel_padding(
            payload.input_image_b64,
            payload.left_pixels,
            payload.right_pixels,
            payload.top_pixels,
            payload.bottom_pixels,
        ),
        mask_image_b64=create_mask(
            payload.input_image_b64,
            payload.left_pixels,
            payload.right_pixels,
            payload.top_pixels,
            payload.bottom_pixels,
        ),
        prompt=payload.prompt,
        model="imagen-3.0-capability-001",
        mask_dilation=payload.mask_dilation,
    )
    try:
        response = await google_service.outpaint(data)
        return response
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=str(e),
        )