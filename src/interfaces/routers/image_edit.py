from fastapi import APIRouter


image_edit_router = APIRouter(prefix="/image_edit", tags=["image_edit"])



@image_edit_router.get(
    path="/outpaint",
    summary="Expand an image",
    
)

async def outpaint():
    return {"Hello": "World"}

