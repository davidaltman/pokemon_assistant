"""
Main FastAPI application module for the Pokemon Chat API.

This module sets up the FastAPI application with CORS middleware and defines
the API endpoints for chat and Pokemon data retrieval.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .chat_service import get_pokemon_response
from .chat_service import get_pokemon_name
from .pokemon_service import get_pokemon_data
import logging

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

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

class MessageRequest(BaseModel):
    """
    Pydantic model for message request payload.

    Attributes:
        message (str): The user's input message that might contain a Pokemon name
    """
    message: str

@app.post("/api/pokemon-from-message")
async def pokemon_from_message(request: MessageRequest):
    """
    Extract a Pokemon name from a message and retrieve its data.

    Args:
        request (MessageRequest): The request containing the user's message

    Returns:
        dict: Pokemon data if a Pokemon name is found, or an error message if not
    """
    logger.info(f"Received message: {request.message}")
    pokemon_name = await get_pokemon_name(request.message)
    logger.info(f"Extracted Pokemon name: {pokemon_name or 'None'}")

    if not pokemon_name:
        logger.warning("No Pokemon name found in message")
        return {"error": "No Pokemon name found in message"}

    pokemon_data = await get_pokemon_data(pokemon_name)
    logger.info(f"Retrieved data for Pokemon: {pokemon_name}")
    return pokemon_data