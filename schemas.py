from pydantic import BaseModel
from typing import List


class BlogPostCreate(BaseModel):
    title: str
    content: str
    category: str
    tags: List[str]


class BlogPostResponse(BlogPostCreate):
    id: int
    createdAt: str
    updatedAt: str