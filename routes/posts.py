from fastapi import APIRouter, HTTPException, Query
from typing import List
from datetime import datetime

from schemas import BlogPostCreate, BlogPostResponse

router = APIRouter()

# Temporary database
posts = []
post_id = 1


# CREATE POST
@router.post("/", response_model=BlogPostResponse, status_code=201)
def create_post(post: BlogPostCreate):
    global post_id

    now = datetime.utcnow().isoformat() + "Z"

    new_post = {
        "id": post_id,
        "title": post.title,
        "content": post.content,
        "category": post.category,
        "tags": post.tags,
        "createdAt": now,
        "updatedAt": now
    }

    posts.append(new_post)
    post_id += 1

    return new_post


# GET ALL POSTS (with optional search)
@router.get("/", response_model=List[BlogPostResponse])
def get_posts(term: str = Query(None)):
    if term:
        term_lower = term.lower()
        return [
            post for post in posts
            if term_lower in post["title"].lower()
            or term_lower in post["content"].lower()
            or term_lower in post["category"].lower()
        ]

    return posts


# GET SINGLE POST
@router.get("/{post_id}", response_model=BlogPostResponse)
def get_post(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return post

    raise HTTPException(status_code=404, detail="Post not found")


# UPDATE POST
@router.put("/{post_id}", response_model=BlogPostResponse)
def update_post(post_id: int, updated_post: BlogPostCreate):
    for post in posts:
        if post["id"] == post_id:
            post["title"] = updated_post.title
            post["content"] = updated_post.content
            post["category"] = updated_post.category
            post["tags"] = updated_post.tags
            post["updatedAt"] = datetime.utcnow().isoformat() + "Z"

            return post

    raise HTTPException(status_code=404, detail="Post not found")


# DELETE POST
@router.delete("/{post_id}", status_code=204)
def delete_post(post_id: int):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts.pop(index)
            return

    raise HTTPException(status_code=404, detail="Post not found")