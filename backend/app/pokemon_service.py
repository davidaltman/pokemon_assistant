"""
Service module for retrieving Pokemon data from the PokeAPI.

This module provides functionality to fetch and format Pokemon information
from the external PokeAPI service.
"""

import requests
from typing import Dict, Any

async def get_pokemon_data(pokemon_name: str) -> Dict[str, Any]:
    """
    Fetch and format Pokemon data from the PokeAPI.

    Args:
        pokemon_name (str): The name of the Pokemon to look up

    Returns:
        Dict[str, Any]: A dictionary containing formatted Pokemon data with the following keys:
            - name: The Pokemon's name
            - id: The Pokemon's Pokedex number
            - height: The Pokemon's height
            - weight: The Pokemon's weight
            - types: List of the Pokemon's types
            - abilities: List of the Pokemon's abilities
            - sprite: URL to the Pokemon's official artwork

            Or in case of an error:
            - error: Error message describing what went wrong

    Example:
        >>> await get_pokemon_data("pikachu")
        {
            "name": "pikachu",
            "id": 25,
            "height": 4,
            "weight": 60,
            "types": ["electric"],
            "abilities": ["static", "lightning-rod"],
            "sprite": "https://raw.githubusercontent.com/..."
        }
    """
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
        response.raise_for_status()
        data = response.json()

        return {
            "name": data["name"],
            "id": data["id"],
            "height": data["height"],
            "weight": data["weight"],
            "types": [t["type"]["name"] for t in data["types"]],
            "abilities": [a["ability"]["name"] for a in data["abilities"]],
            "sprite": data["sprites"]["other"]["official-artwork"]["front_default"]
        }
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch Pokémon data: {str(e)}"}