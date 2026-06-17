from fastapi import APIRouter

router = APIRouter()


@router.post("/generate")
def create_story(request: dict):
    return {
        "success": True,
        "received": request
    }
