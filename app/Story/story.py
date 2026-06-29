from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from app.Story.story_schema import StoryRequest
from app.Story.openai_service import generate_story

router = APIRouter()


@router.post("/generate", response_class=PlainTextResponse)
def create_story(request: StoryRequest):
    story = generate_story(request.prompt)
    return story
