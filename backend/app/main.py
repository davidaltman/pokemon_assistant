from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from .chat_service import get_pokemon_response
from .pokemon_service import get_pokemon_data

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/api/chat")
async def chat(request: ChatRequest):
    response = await get_pokemon_response(request.message)
    return {"response": response}

@app.get("/api/pokemon/{pokemon_name}")
async def get_pokemon(pokemon_name: str):
    pokemon_data = await get_pokemon_data(pokemon_name)
    return pokemon_data