from fastapi import FastAPI
from app.Story.story import router

app = FastAPI(
    title="AI Story Generator API"
)

app.include_router(
    router,
    prefix="/api/v1/story",
    tags=["Story"]
)


@app.get("/")
def home():
    return {"message": "API Running"}
