from fastapi import APIRouter
from app.Story.story_schema import StoryRequest
from app.Story.openai_service import generate_story

router = APIRouter()


def extract_section(text, start, end=None):
    if start not in text:
        return ""

    section = text.split(start, 1)[1]

    if end and end in section:
        section = section.split(end, 1)[0]

    return section.strip()


@router.post("/generate")
def create_story(request: StoryRequest):

    story = generate_story(request.prompt)

    title = extract_section(story, "Title:", "Beginning:")
    beginning = extract_section(story, "Beginning:", "Middle:")
    middle = extract_section(story, "Middle:", "Ending:")
    ending = extract_section(story, "Ending:", "Moral:")
    moral = extract_section(story, "Moral:")

    return {
        "success": True,
        "story": {
            "title": title,
            "beginning": beginning,
            "middle": middle,
            "ending": ending,
            "moral": moral
        }
    }
