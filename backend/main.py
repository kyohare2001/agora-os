from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Agora AI",
    description="A platform for thoughtful dialogue and intellectual exploration",
    version="0.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

# Models
class Thought(BaseModel):
    id: Optional[str] = None
    content: str
    author_id: str
    parent_id: Optional[str] = None
    created_at: Optional[str] = None

class ThoughtResponse(BaseModel):
    id: str
    content: str
    author_id: str
    parent_id: Optional[str] = None
    created_at: str
    children: List['ThoughtResponse'] = []

# Routes
@app.get("/")
async def root():
    return {"message": "Welcome to Agora AI"}

@app.post("/thoughts", response_model=ThoughtResponse)
async def create_thought(thought: Thought):
    # TODO: Implement thought creation with database
    return {
        "id": "1",
        "content": thought.content,
        "author_id": thought.author_id,
        "parent_id": thought.parent_id,
        "created_at": "2024-04-01T00:00:00Z",
        "children": []
    }

@app.get("/thoughts/{thought_id}", response_model=ThoughtResponse)
async def get_thought(thought_id: str):
    # TODO: Implement thought retrieval with database
    if thought_id != "1":
        raise HTTPException(status_code=404, detail="Thought not found")
    return {
        "id": thought_id,
        "content": "Sample thought",
        "author_id": "user1",
        "parent_id": None,
        "created_at": "2024-04-01T00:00:00Z",
        "children": []
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 