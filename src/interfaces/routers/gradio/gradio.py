from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException

from src.application.dtos.response_dtos import ResponseDataDictDTO
from src.domain.schema.image_edit_payload import ImgExpandPayloadV2
from src.application.services.external import GradioService



def getGradioService() -> GradioService:
    """Dependency to get the GradioService instance."""
    return GradioService("jallenjia/flux-fill-outpaint")


gradio_router: APIRouter = APIRouter(
    prefix="/gradio",
    tags=["Gradio"],
    responses={404: {"description": "Not found"}},
)

@gradio_router.post(
    path="/outpaint",
    summary="Outpaint function using Flux Fill Outpaint AI tool",
    response_model=ResponseDataDictDTO,
)
async def outpaint_image(
    payload: ImgExpandPayloadV2,
    gradio_service: GradioService = Depends(getGradioService),
) -> ResponseDataDictDTO:
    """Endpoint to outline an image using Vertex AI."""
    print("payload: ", payload)
    try:
        response = await gradio_service.outpaint(payload)
        return response
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=str(e),
        )
    

# {
#   "message": "Image outpainted successfully",
#   "timestamp": "2025-08-04T08:12:56.923226+00:00",
#   "data": {
#     "generated_image_b64": [
#       "/tmp/gradio/4cf6208dade6974316fe2b581dc8ffc4bb7afe983ea78052b63e455cf908c903/image.webp",
#       "/tmp/gradio/5aca694f030cb0a0696a88feb51118b3bd5d2f2b127e94939076db84a3017a92/image.webp"
#     ],
#     "image_data": {
#       "path": "https://scotland-landscapes.com/wp-content/uploads/2021/12/20200202-DSC08175_1920px-400x300.jpg",
#       "meta": {
#         "_type": "gradio.FileData"
#       },
#       "orig_name": "20200202-DSC08175_1920px-400x300.jpg",
#       "url": "https://scotland-landscapes.com/wp-content/uploads/2021/12/20200202-DSC08175_1920px-400x300.jpg"
#     }
#   }
# }