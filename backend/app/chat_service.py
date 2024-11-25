import openai
import os
from dotenv import load_dotenv
from .pokemon_service import get_pokemon_data

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def get_pokemon_name(message: str) -> str:
    """
    Extract a Pokemon name from a user message using OpenAI's GPT model,
    handling misspellings and variations.

    Args:
        message (str): The user's input message that might contain a Pokemon name

    Returns:
        str: The correctly spelled Pokemon name, or empty string if no Pokemon
             name is found
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {
                    "role": "system",
                    "content": """You are a Pokemon name extractor.
                    Your only job is to find Pokemon names in messages, even if they're misspelled.
                    If you find a Pokemon name, return ONLY the correct spelling of the name in lowercase.
                    If no Pokemon name is found, return 'none'.
                    Examples:
                    'Tell me about pikachu' -> 'pikachu'
                    'What is pikachoo' -> 'pikachu'
                    'What is the weather' -> 'none'"""
                },
                {
                    "role": "user",
                    "content": message
                }
            ],
            temperature=0,
            max_tokens=50
        )

        pokemon_name = response.choices[0].message.content.strip().lower()
        return '' if pokemon_name == 'none' else pokemon_name

    except Exception as e:
        return ''

async def get_pokemon_response(message: str) -> str:
    """
    Generate a response about Pokemon based on user message using OpenAI's GPT model.

    This function attempts to extract a Pokemon name from the user's message,
    fetches relevant Pokemon data, and generates a detailed response using
    the OpenAI chat completion API.

    Args:
        message (str): The user's input message containing a Pokemon-related query

    Returns:
        str: A detailed response about the Pokemon, or an error message if the
             process fails

    Raises:
        Exception: Propagates any exceptions that occur during API calls or
                  data processing
    """
    try:
        # Try to extract Pokemon name from the message
        import re
        pokemon_name_match = re.search(r'(?:about|is|pokemon)\s+(\w+)', message.lower())
        pokemon_info = ""

        if pokemon_name_match:
            pokemon_name = pokemon_name_match.group(1)
            pokemon_data = await get_pokemon_data(pokemon_name)

            if 'error' not in pokemon_data:
                pokemon_info = f"""
                Here are the details about {pokemon_name}:
                - Type(s): {', '.join(pokemon_data['types'])}
                - Height: {pokemon_data['height']/10}m
                - Weight: {pokemon_data['weight']/10}kg
                - Abilities: {', '.join(pokemon_data['abilities'])}
                """

        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {
                    "role": "system",
                    "content": """You are a helpful Pokémon expert assistant.
                    Provide accurate and engaging information about Pokémon.
                    When answering questions, consider the Pokémon's characteristics
                    and provide interesting facts and explanations."""
                },
                {
                    "role": "user",
                    "content": f"{message}\n\nPokemon Data:\n{pokemon_info}"
                }
            ],
            temperature=0.7,
            max_tokens=300
        )

        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"