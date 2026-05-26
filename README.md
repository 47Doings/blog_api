# Blogging Platform API (FastAPI)

A simple RESTful API for a personal blogging platform built with FastAPI. It supports full CRUD operations and search functionality.


## Features

- Create a blog post
- Get all blog posts
- Get a single blog post
- Update a blog post
- Delete a blog post
- Search blog posts by title, content, or category
- Input validation using Pydantic
- Auto-generated API documentation (Swagger UI)


## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic

## How to Run the Project

### 1. Install dependencies
pip install fastapi uvicorn



### 2. Start the server
python -m uvicorn main:app --reload



### 3. Open in browser
API: http://127.0.0.1:8000  
Swagger Docs: http://127.0.0.1:8000/docs  



## API Endpoints

POST /posts → Create Post  
GET /posts → Get All Posts  
GET /posts/{post_id} → Get Single Post  
PUT /posts/{post_id} → Update Post  
DELETE /posts/{post_id} → Delete Post  
GET /posts?term=tech → Search Posts  



## Example Request (Create Post)

POST /posts
{
  "title": "First Post",
  "content": "Learning FastAPI step by step",
  "category": "Tech",
  "tags": ["fastapi", "python"]
}



## Example Response

{
  "id": 1,
  "title": "First Post",
  "content": "Learning FastAPI step by step",
  "category": "Tech",
  "tags": ["fastapi", "python"],
  "createdAt": "2026-05-04T15:20:19Z",
  "updatedAt": "2026-05-04T15:20:19Z"
}



## How to Test (Swagger UI)

1. Run server:
python -m uvicorn main:app --reload

2. Open:
http://127.0.0.1:8000/docs

3. Test:
- POST → create post  
- GET → all posts  
- GET /{id} → single post  
- PUT → update post  
- DELETE → delete post  
- GET ?term= → search  



## What I Learned

- REST API design
- CRUD operations
- HTTP methods (GET, POST, PUT, DELETE)
- Status codes
- Pydantic validation
- FastAPI routing
- Swagger testing



## Author

Built while learning backend development with FastAPI.
