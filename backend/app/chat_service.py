import openai
import os
from dotenv import load_dotenv
from .pokemon_service import get_pokemon_data

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def get_pokemon_response(message: str) -> str:
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