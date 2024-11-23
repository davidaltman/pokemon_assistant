"""
Main FastAPI application module for the Pokemon Chat API.

This module sets up the FastAPI application with CORS middleware and defines
the API endpoints for chat and Pokemon data retrieval.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
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
    """
    Pydantic model for chat request payload.

    Attributes:
        message (str): The user's input message for the chat
    """
    message: str

@app.post("/api/chat")
async def chat(request: ChatRequest):
    """
    Process a chat message and return an AI-generated response about Pokemon.

    Args:
        request (ChatRequest): The chat request containing the user's message

    Returns:
        dict: A dictionary containing the AI response with key 'response'
    """
    response = await get_pokemon_response(request.message)
    return {"response": response}

@app.get("/api/pokemon/{pokemon_name}")
async def get_pokemon(pokemon_name: str):
    """
    Retrieve detailed information about a specific Pokemon.

    Args:
        pokemon_name (str): The name of the Pokemon to look up

    Returns:
        dict: Pokemon data including stats, types, and other information
    """
    pokemon_data = await get_pokemon_data(pokemon_name)
    return pokemon_data