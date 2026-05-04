from fastapi import FastAPI
from routes.posts import router as posts_router

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Blogging API is running"}


app.include_router(posts_router, prefix="/posts", tags=["Posts"])